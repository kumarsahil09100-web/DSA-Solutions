# INTEST - Rating 420

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T17:22:06.326Z  

```py
# cook your dish here
# cook your dish here
T = int(input())
for _ in range(T):
    N = input().strip()
    
    # The first digit is at index 0, and the last digit is at the last index (-1)
    first_digit = int(N[0])
    last_digit = int(N[-1])
    
    print(first_digit + last_digit)
    

```

---

[View on CodeChef](https://www.codechef.com/problems/INTEST)