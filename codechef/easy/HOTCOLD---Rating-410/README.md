# HOTCOLD - Rating 410

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T14:30:19.378Z  

```py
# cook your dish here

X, Y = input().split()
X = int(X)
Y = float(Y)
if X % 5 == 0 and Y >= X + 0.50:
    Y -= (X + 0.50)
print(f"{Y:.2f}")
```

---

[View on CodeChef](https://www.codechef.com/problems/HOTCOLD)