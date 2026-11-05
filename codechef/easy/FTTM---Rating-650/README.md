# FTTM - Rating 650

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Find the Term

You are given a string $S$ and another string $T$.

Your task is to determine whether $T$ appears in $S$ as a  **contiguous substring**.

The search is case-sensitive, so uppercase and lowercase letters are considered different.

Print `YES` if $T$ occurs in $S$; otherwise, print `NO`.

### Input Format
- The first line contains the string $S$.
- The second line contains the string $T$.
### Output Format
- Print YES if $T$ is present in $S$, Otherwise, print NO.
### Constraints
- $1 \le |S| \le 1000$
- $1 \le |T| \le 100$
- The search is case-sensitive.
### Sample 1:
Input
Output

```
The quick brown fox jumps over the lazy dog
brown
```

```
YES
```

### Explanation:

The string `brown` appears as a contiguous substring of $S$.

Therefore, the answer is `YES`.

### Sample 2:
Input
Output

```
Competitive Programming
programming
```

```
NO
```

### Explanation:

The search is case-sensitive. The string contains `Programming`, but not `programming`.

Therefore, the answer is `NO`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-05T12:37:04.110Z  

```py
# cook your dish here
s = input()
t = input()
if t in s:
    print("yes")
else:
    print("no")
```

---

[View on CodeChef](https://www.codechef.com/problems/FTTM)