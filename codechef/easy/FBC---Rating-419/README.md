# FBC - Rating 419

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Fill the Bucket

Chef has a bucket having a capacity of $K$ liters. It is already filled with $X$ liters of water.

Find the  **maximum**  amount of extra water in liters that Chef can fill in the bucket without overflowing.

### Input Format
- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space separated integers $K$ and $X$ - as mentioned in the problem.
### Output Format

For each test case, output in a single line, the amount of extra water in liters that Chef can fill in the bucket without overflowing.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X \lt K \leq 1000$
### Sample 1:
Input
Output

```
2
5 4
15 6

```

```
1
9

```

### Explanation:

 **Test Case $1$:**  The capacity of the bucket is $5$ liters but it is already filled with $4$ liters of water. Adding $1$ more liter of water to the bucket fills it to $(4+1) = 5$ liters. If we try to fill more water, it will overflow.

 **Test Case $2$:**  The capacity of the bucket is $15$ liters but it is already filled with $6$ liters of water. Adding $9$ more liters of water to the bucket fills it to $(6+9) = 15$ liters. If we try to fill more water, it will overflow.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T13:05:23.789Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    k,x = map(int,input().split())
    print(k-x)
```

---

[View on CodeChef](https://www.codechef.com/problems/FBC)