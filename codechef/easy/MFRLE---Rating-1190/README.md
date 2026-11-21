# MFRLE - Rating 1190

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-21T15:16:40.113Z  

```py
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



```

---

[View on CodeChef](https://www.codechef.com/problems/MFRLE)