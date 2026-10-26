# DOMINANT - Rating 488

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Dominant Army

In the medieval age, there were $3$ kingdoms $A$, $B$, and $C$. The army of these kingdom had $N_A$, $N_B$, and $N_C$ soldiers respectively.

You are given that an army with $X$ soldiers can defeat an army with $Y$ soldiers only if $X \gt Y$.

An army is said to be  **dominant**  if it can defeat both the other armies  **combined**. For example, kingdom $C$'s army will be dominant only if $N_C > N_A + N_B$.

Determine whether any of the armies is  **dominant**  or not.

### Input Format
- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains three integers $N_A$, $N_B$, and $N_C$ - the number of warriors in the armies of kingdoms $A$, $B$, and $C$ respectively.
### Output Format

For each test case, output `YES` if any of the armies is dominant. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq N_A, N_B, N_C \leq 100$
### Sample 1:
Input
Output

```
4
15 5 6
12 13 16
1 1 100
10 10 20

```

```
YES
NO
YES
NO

```

### Explanation:

 **Test case $1$:**  The kingdom $A$'s army is dominant since $15 > 5 + 6$.

 **Test case $2$:**  We can observe that none of the armies is dominant.

 **Test case $3$:**  The kingdom $C$'s army is dominant since $100 > 1 + 1$.

 **Test case $4$:**  We can observe that none of the armies is dominant. Note that the kingdom $C$'s army is not dominant since $20 \le 10 + 10$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-26T14:31:40.004Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    a,b,c = map(int, input().split())
    if(a>b+c or b>a+c or c>b+a):
        print("yes")
    else:
        print("no")
    

```

---

[View on CodeChef](https://www.codechef.com/problems/DOMINANT)