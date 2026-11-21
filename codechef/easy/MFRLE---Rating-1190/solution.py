# cook your dish here

s = input()

freq = {}

for i in range(len(s) - 1):
    pair = s[i:i+2]
    freq[pair] = freq.get(pair, 0) + 1

ans = 0

for count in freq.values():
    if count >= 2:
        ans += 1

print(ans)


