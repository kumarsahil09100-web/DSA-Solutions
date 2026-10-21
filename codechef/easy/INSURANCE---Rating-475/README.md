# INSURANCE - Rating 475

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Insurance

Chef bought car insurance. The policy of the insurance is:

- The maximum rebatable amount for any damage is Rs $X$ lakhs.
- If the amount required for repairing the damage is $\leq X$ lakhs, that amount is rebated in full.

Chef's car meets an accident and required Rs $Y$ lakhs for repairing.

Determine the amount that will be rebated by the insurance company.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains two space-separated integers $X$ and $Y$.
### Output Format

For each test case, output the amount (in lakhs) that will be rebated by the insurance company.

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq X, Y \leq 30$
### Sample 1:
Input
Output

```
4
5 3
5 8
4 4
15 12

```

```
3
5
4
12

```

### Explanation:

 **Test case $1$:**  The damages require only Rs $3$ lakh which is below the upper cap, so the entire Rs $3$ lakh will be rebated.

 **Test case $2$:**  The damages require Rs $8$ lakh which is above the upper cap, so only Rs $5$ lakh will be rebated.

 **Test case $3$:**  The damages require only Rs $4$ lakh which is equal to the upper cap, so the whole Rs $4$ lakh will be rebated.

 **Test case $4$:**  The damages require Rs $15$ lakh which is above the upper cap, so only Rs $12$ lakh will be rebated.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-21T13:23:38.158Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    if(x>=y):
        print(y)
    else:
        print(x)

```

---

[View on CodeChef](https://www.codechef.com/problems/INSURANCE)