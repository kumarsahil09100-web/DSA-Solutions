# COUGAME - Rating 347

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Couple Game

There are $G$ girl and $B$ boy students at IIT (BHU) such that $B \gt G$.

If ICM were a team game where teams could only be of size $2$, having  **exactly**  $1$ girl student and $1$ boy student, what would be the  **minimum**  number of boy students from IIT (BHU) who would not be able to participate?

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains two space-separated integers $G$ and $B$, the number of girl and boy students at IIT (BHU) respectively.
### Output Format

For each test case, output a single integer on a new line, the  **minimum**  number of boy students from IIT (BHU) who would not be able to participate.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq G \lt B \leq 100$
### Sample 1:
Input
Output

```
3
1 3
2 4
3 10
```

```
2
2
7
```

### Explanation:

 **Test case $1$:**  There is only $1$ girl and $3$ boys. So, one team can be formed, and minimum $2$ boys will be left behind.

 **Test case $2$:**  There are $2$ girls and $4$ boys. So, maximum $2$ teams can be formed, and minimum $2$ boys will be left behind.

 **Test case $3$** : There are $3$ girls and $10$ boys. So, maximum $3$ teams can be formed, and minimum $7$ boys will be left behind.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-09T18:03:06.444Z  

```py
# cook your dish here
t =int(input())
while t>0:
    g,b = map(int,input().split())
    print(b-g)
    t -=1
```

---

[View on CodeChef](https://www.codechef.com/problems/COUGAME)