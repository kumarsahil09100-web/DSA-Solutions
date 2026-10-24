# CGYM - Rating 493

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T16:25:20.285Z  

```py
# cook your dish here
t = int(input())
for i  in range(t):
    a,b,c,x = map(int , input().split())
    if(a+b>=x or a+c>=x or c+b>=x):
        print("yes")
    else:
        print("no")
```

---

[View on CodeChef](https://www.codechef.com/problems/CGYM)