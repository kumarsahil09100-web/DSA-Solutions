# INTRDSGN - Rating 373

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Interior Design

Chef decided to redecorate his house, and now needs to decide between two different styles of interior design.

For the first style, tiling the floor will cost $X_1$ rupees and painting the walls will cost $Y_1$ rupees.

For the second style, tiling the floor will cost $X_2$ rupees and painting the walls will cost $Y_2$ rupees.

Chef will choose whichever style has the lower total cost. How much will Chef pay for his interior design?

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input, containing $4$ space-separated integers $X_1, Y_1, X_2, Y_2$ as described in the statement.
### Output Format

For each test case, output on a new line the amount Chef will pay for interior design.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X_1, Y_1, X_2, Y_2 \leq 100$
### Sample 1:
Input
Output

```
4
10 20 9 25
10 20 9 20
10 20 20 10
100 43 85 61

```

```
30
29
30
143
```

### Explanation:

 **Test case $1$:**  The first style costs $10 + 20 = 30$ rupees, and the second costs $9 + 25 = 34$ rupees. The first is cheaper, so Chef will pay $30$ rupees.

 **Test case $2$:**  The first style costs $10 + 20 = 30$ rupees, and the second costs $9 + 20 = 29$ rupees. The second is cheaper, so Chef will pay $29$ rupees.

 **Test case $3$:**  The first style costs $10 + 20 = 30$ rupees, and the second costs $20 + 10 = 30$ rupees. Both styles cost the same, so Chef is always going to pay $30$ rupees.

 **Test case $4$:**  The first style costs $100 + 43 = 143$ rupees, and the second costs $85 + 61 = 146$ rupees. The first is cheaper, so Chef will pay $143$ rupees.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T17:23:44.215Z  

```py
# cook your dish here
# cook your dish here
t = int(input())
for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    print(min(x1 + y1, x2 + y2))

```

---

[View on CodeChef](https://www.codechef.com/problems/INTRDSGN)