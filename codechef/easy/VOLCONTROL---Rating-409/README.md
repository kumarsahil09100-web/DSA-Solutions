# VOLCONTROL - Rating 409

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Volume Control

Chef is watching TV. The current volume of the TV is $X$. Pressing the `volume up` button of the TV remote increases the volume by $1$ while pressing the `volume down` button decreases the volume by $1$. Chef wants to change the volume from $X$ to $Y$. Find the minimum number of button presses required to do so.

### Input Format
- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $X$ and $Y$ - the initial volume and final volume of the TV.
### Output Format

For each test case, output the minimum number of times Chef has to press a button to change the volume from $X$ to $Y$.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X, Y \leq 100$
### Sample 1:
Input
Output

```
2
50 54
12 10

```

```
4
2

```

### Explanation:

 **Test Case 1:**  Chef can press the `volume up` button $4$ times to increase the volume from $50$ to $54$.

 **Test Case 2:**  Chef can press the `volume down` button $2$ times to decrease the volume from $12$ to $10$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T14:25:18.876Z  

```py
# cook your dish here
t = int(input())
for i  in range(t):
    x,y =map(int,input().split())
    if(x>y):
        print(x-y)
    else:
        print(y-x)


```

---

[View on CodeChef](https://www.codechef.com/problems/VOLCONTROL)