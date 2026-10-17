# DISCNT - Rating 399

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T14:08:17.645Z  

```py
# cook your dish here

t =  int(input())
for i in range(t):
    x,y = map(int, input().split())
    if(x>y):
        print("second")
    elif(y>x):
        print("first")
    else:
        print("any")
```

---

[View on CodeChef](https://www.codechef.com/problems/DISCNT)