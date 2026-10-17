# DISCNT - Rating 401

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Discount

Alice buys a toy with a selling price of $100$ rupees. There is a discount of $x$ percent on the toy. Find the amount Alice needs to pay for it.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains a single integer, $x$ — the discount on the toy.
### Output Format

For each test case, output on a new line the price that Alice needs to pay.

### Constraints
- $1 \leq T \leq 100$
- $0 \leq x \lt 100$
### Sample 1:
Input
Output

```
4
5
9
11
21

```

```
95
91
89
79

```

### Explanation:

 **Test case $1$:**  The discount is $5$ percent, i.e. $5$ rupees. So, Alice will have to pay $100-5=95$ rupees.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T14:10:40.761Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    x = int(input())
    print(100-x)

```

---

[View on CodeChef](https://www.codechef.com/problems/DISCNT)