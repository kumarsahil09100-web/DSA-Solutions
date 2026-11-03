# cook your dish here
s = input()
s = s.lower()
freq  = {}
for ch in s:
    if ch.isalpha():
        freq[ch]=freq.get(ch,0)+1
ans = min(freq,key = lambda x :(-freq[x],x))
print(ans)
    