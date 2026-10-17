# CABS - Rating 399

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### The Cheaper Cab

Chef has to travel to another place. For this, he can avail any one of two cab services.

- The first cab service charges $X$ rupees.
- The second cab service charges $Y$ rupees.

Chef wants to spend the  **minimum**  amount of money. Which cab service should Chef take?

### Input Format
- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $X$ and $Y$ - the prices of first and second cab services respectively.
### Output Format

For each test case, output `FIRST` if the first cab service is cheaper, output `SECOND` if the second cab service is cheaper, output `ANY` if both cab services have the same price.

You may print each character of `FIRST`, `SECOND` and `ANY` in uppercase or lowercase (for example, `any`, `aNy`, `Any` will be considered identical).

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X, Y \leq 100$
### Sample 1:
Input
Output

```
3
30 65
42 42
90 50

```

```
FIRST
ANY
SECOND

```

### Explanation:

 **Test case $1$:**  The first cab service is cheaper than the second cab service.

 **Test case $2$:**  Both the cab services have the same price.

 **Test case $3$:**  The second cab service is cheaper than the first cab service.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T14:08:15.530Z  

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

[View on CodeChef](https://www.codechef.com/problems/CABS)