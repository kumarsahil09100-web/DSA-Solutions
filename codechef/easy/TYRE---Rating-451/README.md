# TYRE - Rating 451

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T13:37:40.129Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    if(x>y):
        print("NEW PHONE")
    elif(y>x):
        print("repair")
    else:
        print("any")

```

---

[View on CodeChef](https://www.codechef.com/problems/TYRE)