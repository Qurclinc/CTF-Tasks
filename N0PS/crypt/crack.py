import socket
import string

# STRINGS = "N1234567890_-qwertyuiop[]{}asdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBM"
# STRINGS = "N0PS{u5u4L_M1sT4k3S" + string.printable
STRINGS = string.printable

sock = socket.socket()
sock.connect(('0.cloud.chals.io', 31561))

msg = sock.recv(1024).decode("utf-8")
flag = msg.split("\n")[2].split(":")[1].strip()
cur_msg = ""
# cur_msg = "N0PS{u5u4L_M1sT4k3S"

print(msg)
# print(msg, flag, sep="\n\n")

for _ in range(23):
    for sym in STRINGS:
        sock.send((cur_msg + sym + "\n").encode())
        res = sock.recv(2048).decode("utf-8").split("\n")[0]
        # print(res)
        # print(flag[:(len(cur_msg) + 1) * 2])
        if res == flag[:(len(cur_msg) + 1) * 2]:
            print(sym)
            cur_msg += sym
            continue
    # print("!!!", " ", cur_msg)

sock.close()
