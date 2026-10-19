# FLOW006 - Rating 455

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Sum of Digits

You're given an integer  **N**. Write a program to calculate the sum of all the digits of  **N**.

### Input Format

The first line contains an integer  **T**, the total number of testcases. Then follow  **T**  lines, each line contains an integer  **N**.

### Output Format

For each test case, calculate the sum of digits of  **N**, and display it in a new line.

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000000$
### Sample 1:
Input
Output

```
3 
12345
31203
2123

```

```
15
9
8

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T13:53:37.896Z  

```py
# cook your dish here
t =int(input())
for i in range(t):
    n = input()
    sum =0
    for char in n:
         sum +=int(char)
    print(sum)
        
        
    


```

---

[View on CodeChef](https://www.codechef.com/problems/FLOW006)