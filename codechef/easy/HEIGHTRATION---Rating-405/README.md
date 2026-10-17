# HEIGHTRATION - Rating 405

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Height of Rationals

In a recent breakthrough in mathematics, the proof utilized a concept called `Height`.

Consider a fraction $\frac{a}{b}$. Its `Height` is defined as the  **maximum**  of its numerator and denominator. So, for example, the `Height` of $\frac{3}{19}$ would be $19$, and the `Height` of $\frac{27}{4}$ would be $27$.

Given $a$ and $b$, find the `Height` of $\frac{a}{b}$.

### Input Format

The only line of input contains two integers, $a$ and $b$.

### Output Format

Output a single integer, which is the `Height` of $\frac{a}{b}$.

### Constraints
- $1 \leq a, b \leq 100$
- $a$ and $b$ do not have any common factors.
### Sample 1:
Input
Output

```
3 19

```

```
19

```

### Explanation:

The maximum of $\{3, 19\}$ is $19$. Hence the `Height` of $\frac{3}{19}$ is $19$.

### Sample 2:
Input
Output

```
27 4

```

```
27

```

### Explanation:

The maximum of $\{27, 4\}$ is $27$. Hence the `Height` of $\frac{27}{4}$ is $27$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T14:15:11.979Z  

```py
# cook your dish here
a,b = map(int,input().split())
if(a>b):
    print(a)
else:
    print(b)

```

---

[View on CodeChef](https://www.codechef.com/problems/HEIGHTRATION)