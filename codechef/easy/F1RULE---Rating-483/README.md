# F1RULE - Rating 483

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T15:00:19.207Z  

```py
# cook your dish here
t =  int(input())
for i in range(t):
    w,x,y,z = map(int,input().split())
    if(w+(y*z)>x):
        print("overflow")
    elif(w+(y*z)<x):
        print("unfilled")
    else:
        print("filled")

```

---

[View on CodeChef](https://www.codechef.com/problems/F1RULE)