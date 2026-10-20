# CREDSCORE - Rating 459

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Credit score

To access CRED programs, one needs to have a credit score of $750$ or more.
Given that the present credit score is $X$, determine if one can access CRED programs or not.

If it is possible to access CRED programs, output $\texttt{YES}$, otherwise output $\texttt{NO}$.

### Input Format

The first and only line of input contains a single integer $X$, the credit score.

### Output Format

Print $\texttt{YES}$ if it is possible to access CRED programs. Otherwise, print $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

### Constraints
- $0 \leq X \leq 1000$
### Subtasks
- Subtask 1 (100 points): Original constraints.
### Sample 1:
Input
Output

```
823
```

```
YES
```

### Explanation:

Since $823 \geq 750$, it is possible to access CRED programs.

### Sample 2:
Input
Output

```
251
```

```
NO
```

### Explanation:

Since $251 \lt 750$, it is not possible to access CRED programs.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-20T14:31:59.591Z  

```py
# cook your dish here
x = int(input())
if(x>=750):
    print("yes")
else:
    print("no")

```

---

[View on CodeChef](https://www.codechef.com/problems/CREDSCORE)