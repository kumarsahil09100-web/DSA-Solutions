# CHEFCHOCO - Rating 492

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef and Chocolates

Chef wants to gift $C$ chocolates to Botswal on his birthday. However, he has only $X$ chocolates with him.
The cost of $1$ chocolate is $Y$ rupees.

Find the  **minimum**  money in rupees Chef needs to spend so that he can gift $C$ chocolates to Botswal.

### Input Format
- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, three integers $C, X,$ and $Y$.
### Output Format

For each test case, output in a single line answer, the  **minimum**  money in rupees Chef needs to spend.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq C \leq 100$
- $0 \leq X \leq C$
- $1 \leq Y \leq 100$
### Sample 1:
Input
Output

```
2
7 5 5
10 1 1
```

```
10
9
```

### Explanation:

 **Test Case $1$:**  Chef has to gift a total of $7$ chocolates out of which he has $5$ chocolates. Thus, Chef needs to buy $2$ more chocolates, which costs him $10$ rupees.

 **Test Case $2$:**  Chef has to gift a total of $10$ chocolates out of which he has $1$ chocolate. Thus, Chef needs to buy $9$ more chocolates, which costs him $9$ rupees.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T14:57:30.280Z  

```py
# cook your dish here
t = int(input())
for  i in range(t):
    c,x,y = map(int, input().split())
    print((c-x)*y)

```

---

[View on CodeChef](https://www.codechef.com/problems/CHEFCHOCO)