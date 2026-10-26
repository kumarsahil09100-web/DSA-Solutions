# MONOPOLY - Rating 482

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Monopoly in Chefland

Chef is the financial incharge of Chefland and one of his duties is identifying if any company has gained a monopolistic advantage in the market.

There are exactly $3$ companies in the market each of whose revenues are denoted by $R_1$, $R_2$ and $R_3$ respectively. A company is said to have a monopolistic advantage if its revenue is  **strictly**  greater than the sum of the revenues of its competitors.

Given the revenue of the $3$ companies, help Chef determine if any of them has a monopolistic advantage.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing three space separated integers $R_1$, $R_2$ and $R_3$ denoting the revenue of the three companies respectively.
### Output Format

For each test case, output $\texttt{YES}$ if any of the companies has a monopolistic advantage over its competitors, else output $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq R_1, R_2, R_3 \leq 10$
### Sample 1:
Input
Output

```
4
1 1 1
1 2 4
2 10 3
1 2 3

```

```
No
Yes
Yes
No

```

### Explanation:

 **Test case 1:**  All the companies have equal revenue so none have a monopolistic advantage.

 **Test case 2:**  The third company has a monopolistic advantage as $1 + 2 < 4$.

 **Test case 3:**  The second company has a monopolistic advantage as $2 + 3 < 10$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-26T14:30:09.199Z  

```py
# cook your dish here
t = int(input())
for i in range (t):
    r1,r2,r3 = map(int,input().split())
    if(r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2):
        print("yes")
    else:
        print("no")
```

---

[View on CodeChef](https://www.codechef.com/problems/MONOPOLY)