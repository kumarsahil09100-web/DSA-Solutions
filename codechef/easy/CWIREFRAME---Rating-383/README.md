# CWIREFRAME - Rating 383

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef and Wire Frames

Chef has a rectangular plate of length $N cm$ and width $M cm$. He wants to make a wireframe around the plate. The wireframe costs $X$ rupees per cm.

Determine the cost Chef needs to incur to buy the wireframe.

### Input Format
- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input, containing three space-separated integers $N,M,$ and $X$ — the length of the plate, width of the plate, and the cost of frame per cm.
### Output Format

For each test case, output in a single line, the price Chef needs to pay for the wireframe.

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq N,M,X \leq 1000$
### Sample 1:
Input
Output

```
3
10 10 10
23 3 12
1000 1000 1000

```

```
400
624
4000000
```

### Explanation:

 **Test case $1$:**  The total length of the frame is $2\cdot 10 + 2\cdot 10 = 40$ cms. Since the cost is $10$ per cm, the total cost would be $10 \cdot 40 = 400$.

 **Test case $2$:**  The total length of the frame is $2\cdot 23 + 2\cdot 3 = 52$ cms. Since the cost is $12$ per cm, the total cost would be $52 \cdot 12 = 624$.

 **Test case $3$:**  The total length of the frame is $2\cdot 1000 + 2\cdot 1000 = 4000$ cms. Since the cost is $1000$ per cm, the total cost would be $4000 \cdot 1000 = 4000000$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-15T13:38:59.819Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    n,m,x = map(int, input().split())
    print(2*(n+m)*x)

```

---

[View on CodeChef](https://www.codechef.com/problems/CWIREFRAME)