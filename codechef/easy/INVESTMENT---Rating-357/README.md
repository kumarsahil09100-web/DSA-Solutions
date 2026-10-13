# INVESTMENT - Rating 357

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Good Investment or Not

Chef has invested his money at an interest rate of $X$ percent per annum while the current inflation rate is $Y$ percent per annum.

An investment is called  *good*  if and only if the interest rate of the investment is  **at least twice**  of the inflation rate.
Determine whether the investment made by Chef is  *good*  or not.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two integers $X$ and $Y$, the interest rate and the current inflation rate respectively.
### Output Format

For each test case, output `YES` if the investment is good, `NO` otherwise.

You can output any letter in any case. For example `YES`, `yes`, `yES` are all considered same.

### Constraints
- $1 \leq T \leq 400$
- $1 \leq X, Y \leq 20$
### Sample 1:
Input
Output

```
5
7 4
6 3
2 4
10 10
20 1

```

```
NO
YES
NO
NO
YES

```

### Explanation:

 **Test case $1$:**  The interest rate is $7$ and the current inflation rate is $4$. Since the interest rate is less than twice of current inflation rate, the investment is not good.

 **Test case $2$:**  The interest rate is $6$ and the current inflation rate is $3$. Since the interest rate is equal to twice of current inflation rate, the investment is good.

 **Test case $3$:**  The interest rate is $2$ and the current inflation rate is $4$. Since the interest rate is less than twice of current inflation rate, the investment is not good.

 **Test case $4$:**  The interest rate is $10$ and the current inflation rate is $10$. Since the interest rate is less than twice of current inflation rate, the investment is not good.

 **Test case $5$:**  The interest rate is $20$ and the current inflation rate is $1$. Since the interest rate is greater than twice of current inflation rate, the investment is good.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T14:07:47.853Z  

```py
# cook your dish here
t = int(input())
for  i in range(t):
    x,y = map(int, input().split())
    if((2*y)<=x):
        print("yes")
    else:
        print("no")

```

---

[View on CodeChef](https://www.codechef.com/problems/INVESTMENT)