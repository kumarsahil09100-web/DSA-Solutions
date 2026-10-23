# SONGS - Rating 488

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T15:22:18.053Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    a,b,c = map(int, input().split())
    if(a>b+c or b>a+c or c>b+a):
        print("yes")
    else:
        print("no")
    

```

---

[View on CodeChef](https://www.codechef.com/problems/SONGS)