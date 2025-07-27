# src = [0x61,0x62,99 ,100,0x65,0x66,0x67,0x68,0x69,0x6a,0x6b,0x6c,0x6d,0x6e,0x6f,0x70,0x71,0x72,0x73,0x74,0x75,0x76,0x77,0x78,0x79,0x7a]
src = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
to = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

d = dict()

for i in range(len(src)):
    d[src[i]] = to[i]


string = "ngx_qkt_fgz_ugffq_uxtll_dt"

for i in range(26):
    new_str = ""
    for el in string:
        try:
            new_str += d[el]
        except KeyError:
            new_str += el
    string = new_str
    print(new_str)
