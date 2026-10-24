# SPECIALITY - Rating 432

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T17:11:52.443Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    if(100*x > 10*y):
        print("cloth")
    elif(100*x < 10*y):
        print("disposable")
    else:
        print("cloth")
```

---

[View on CodeChef](https://www.codechef.com/problems/SPECIALITY)