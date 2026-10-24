# FLOW004 - Rating 420

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### First and Last Digit

Given an integer  **N** . Write a program to obtain the sum of the first and last digits of this number.

### Input Format

The first line contains an integer  **T**, the total number of test cases. Then follow  **T**  lines, each line contains an integer  **N**.

### Output Format

For each test case, display the sum of first and last digits of  **N**  in a new line.

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000000$
### Sample 1:
Input
Output

```
3 
1234
124894
242323

```

```
5
5
5
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T17:21:57.803Z  

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

[View on CodeChef](https://www.codechef.com/problems/FLOW004)