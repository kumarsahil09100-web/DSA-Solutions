# MANIPULATE - Rating 427

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Ezio and Guards

Ezio can manipulate  **at most**  $X$ number of guards with the apple of eden.

Given that there are $Y$ number of guards, predict if he can safely manipulate all of them.

### Input Format
- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $X$ and $Y$.
### Output Format

For each test case, print $\texttt{YES}$ if it is possible for Ezio to manipulate all the guards. Otherwise, print $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X, Y \leq 100$
### Sample 1:
Input
Output

```
3
5 7
6 6
9 1
```

```
NO
YES
YES
```

### Explanation:

 **Test Case $1$:**  Ezio can manipulate at most $5$ guards. Since there are $7$ guards, he cannot manipulate all of them.

 **Test Case $2$:**  Ezio can manipulate at most $6$ guards. Since there are $6$ guards, he can manipulate all of them.

 **Test Case $3$:**  Ezio can manipulate at most $9$ guards. Since there is only $1$ guard, he can manipulate the guard.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T13:14:57.489Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    if(y<=x):
        print("yes")
    else:
        print("no")
```

---

[View on CodeChef](https://www.codechef.com/problems/MANIPULATE)