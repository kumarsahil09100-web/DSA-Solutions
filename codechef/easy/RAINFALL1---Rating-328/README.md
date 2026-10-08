# RAINFALL1 - Rating 328

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Rain in Chefland

In Chefland, precipitation is measured using a rain gauge in millimetre per hour.

Chef categorises rainfall as:

- LIGHT, if rainfall is less than $3$ millimetre per hour.
- MODERATE, if rainfall is greater than equal to $3$ millimetre per hour and less than $7$ millimetre per hour.
- HEAVY if rainfall is greater than equal to $7$ millimetre per hour.

Given that it rains at $X$ millimetre per hour on a day, find whether the rain is `LIGHT`,` MODERATE`, or `HEAVY`.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $X$ — the rate of rainfall in millimetre per hour.
### Output Format

For each test case, output on a new line, whether the rain is `LIGHT`,` MODERATE`, or `HEAVY`.

You may print each character in lowercase or uppercase. For example, `LIGHT`, `light`, `Light`, and `liGHT`, are all identical.

### Constraints
- $1 \leq T \leq 20$
- $1 \leq X \leq 20$
### Sample 1:
Input
Output

```
4
1
20
3
7

```

```
LIGHT
HEAVY
MODERATE
HEAVY
```

### Explanation:

 **Test case $1$:**  The rate of precipitation is less than $3$. Thus, the rain is `LIGHT`.

 **Test case $2$:**  The rate of precipitation is greater than equal to $7$. Thus, the rain is `HEAVY`.

 **Test case $3$:**  The rate of precipitation is greater than equal to $3$ and less than $7$. Thus, the rain is `MODERATE`.

 **Test case $4$:**  The rate of precipitation is greater than equal to $7$. Thus, the rain is `HEAVY`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-08T13:43:14.399Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    x= int(input())
    if(x<3):
        print("light")
    elif (x>=7):
        print("heavy")
    else:
        print("moderate")
```

---

[View on CodeChef](https://www.codechef.com/problems/RAINFALL1)