# TYRE - Rating 452

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Tyre problem

There are $N$ bikes and $M$ cars on the road.

- Each bike has $2$ tyres.
- Each car has $4$ tyres.

Find the total number of tyres on the road.

### Input Format
- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $N, M$.
### Output Format

For each test case, output in a single line, the total number of tyres on the road.

### Constraints
- $1 \leq T \leq 1000$
- $0 \leq N, M \leq 100$
### Sample 1:
Input
Output

```
2
2 1
3 0

```

```
8
6

```

### Explanation:

 **Test Case $1$:**  There are $2$ bikes and $1$ car. Each bike has $2$ tyres, so there are $2\cdot 2 = 4$ bike tyres. Similarly, each car has $4$ tyres, so there are $1\cdot 4 = 4$ car tyres. Adding the tyres of all vehicles, we get $4+4=8$ tyres in total.

 **Test Case $2$:**  There are $3$ bikes and $0$ cars. Each bike has $2$ tyres, so there are $3\cdot 2 = 6$ bike tyres. There are no cars, so there are $0\cdot 4 = 0$ car tyres. Adding the tyres of all vehicles, we get $6+0=6$ tyres in total.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T13:44:30.619Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    print((2*n)+(4*m))

```

---

[View on CodeChef](https://www.codechef.com/problems/TYRE)