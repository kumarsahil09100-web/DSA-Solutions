# SIXFRIENDS - Rating 382

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Six Friends

Six friends go on a trip and are looking for accommodation. After looking for hours, they find a hotel which offers two types of rooms — double rooms and triple rooms. A double room costs Rs. $X$, while a triple room costs Rs. $Y$.

The friends can either get three double rooms or get two triple rooms. Find the minimum amount they will have to pay to accommodate all six of them.

### Input Format
- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $X$ and $Y$ - the cost of a double room and the cost of a triple room.
### Output Format

For each testcase, output the minimum amount required to accommodate all the six friends.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X \lt Y \leq 100$
### Sample 1:
Input
Output

```
3
10 15
6 8
4 8

```

```
30
16
12

```

### Explanation:

 **Test case 1:**  The friends can take three double rooms and thus pay a total of Rs. $30$.

 **Test case 2:**  The friends can take two triple rooms and thus pay a total of Rs. $16$.

 **Test case 3:**  The friends can take three double rooms and thus pay a total of Rs. $12$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-15T13:35:31.732Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    if((3*x)>(2*y)):
        print(2*y)
    else:
        print(3*x)

```

---

[View on CodeChef](https://www.codechef.com/problems/SIXFRIENDS)