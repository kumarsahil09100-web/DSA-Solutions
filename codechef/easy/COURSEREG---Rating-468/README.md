# COURSEREG - Rating 468

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-21T13:08:32.915Z  

```py
# cook your dish here
t = int(input())
for  i in range(t):
    x,y,z = map(int,input().split())
    if(((x*y)/60)<=24*z):
        print("yes")
    else:
        print("no")

```

---

[View on CodeChef](https://www.codechef.com/problems/COURSEREG)