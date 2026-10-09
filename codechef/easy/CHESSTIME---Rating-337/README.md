# CHESSTIME - Rating 337

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chess Time

Chef has recently started playing chess, and wants to play as many games as possible.

He calculated that playing one game of chess takes at least $20$ minutes of his time.

Chef has $N$  **hours**  of free time. What is the maximum number of  **complete**  chess games he can play in that time?

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line containing a single integer, $N$.
### Output Format

For each test case, output on a new line the maximum number of complete chess games Chef can play in $N$ hours.

### Constraints
- $1 \leq T \leq 10$
- $1 \leq N \leq 10$
### Sample 1:
Input
Output

```
4
1
10
7
3

```

```
3
30
21
9

```

### Explanation:

 **Test case $1$:**  If every game Chef plays takes $20$ minutes, he can play $3$ games in one hour.

 **Test case $2$:**  If every game Chef plays takes $20$ minutes, he can play $30$ games in $10$ hours.

 **Test case $3$:**  If every game Chef plays takes $20$ minutes, he can play $21$ games in $7$ hours.

 **Test case $4$:**  If every game Chef plays takes $20$ minutes, he can play $9$ games in $3$ hours.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-09T16:49:12.962Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    print(3*n)
    
    
```

---

[View on CodeChef](https://www.codechef.com/problems/CHESSTIME)