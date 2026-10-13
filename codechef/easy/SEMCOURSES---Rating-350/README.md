# SEMCOURSES - Rating 350

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef and Chapters

This semester, Chef took $X$ courses. Each course has $Y$ units and each unit has $Z$ chapters in it.

Find the total number of chapters Chef has to study this semester.

### Input Format
- The first line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input, containing three space-separated integers $X, Y,$ and $Z$.
### Output Format

For each test case, output in a single line the total number of chapters Chef has to study this semester.

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq X, Y, Z \leq 1000$
### Sample 1:
Input
Output

```
3
1 1 1
2 1 2
1 2 3
```

```
1
4
6
```

### Explanation:

 **Test case $1$:**  There is only $1$ course with $1$ unit. The unit has $1$ chapter. Thus, the total number of chapters is $1$.

 **Test case $2$:**  There are $2$ courses with $1$ unit each. Thus, there are $2$ units. Each unit has $2$ chapters. Thus, the total number of chapters is $4$.

 **Test case $3$:**  There is only $1$ course with $2$ units. Each unit has $3$ chapters. Thus, the total number of chapters is $6$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T13:44:58.240Z  

```py
# cook your dish here
t = int(input())
while(t>0):
    x,y,z = map(int, input().split())
    print(x*y*z)
    t -=1

```

---

[View on CodeChef](https://www.codechef.com/problems/SEMCOURSES)