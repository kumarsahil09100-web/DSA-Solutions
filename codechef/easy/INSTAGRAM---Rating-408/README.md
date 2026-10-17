# INSTAGRAM - Rating 408

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Instagram

Chef categorises an instagram account as  *spam*, if, the  *following*  count of the account is more than $10$ times the count of  *followers*.

Given the  *following*  and  *follower*  count of an account as $X$ and $Y$ respectively, find whether it is a  *spam*  account.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $X$ and $Y$ — the following and follower count of an account, respectively.
### Output Format

For each test case, output on a new line, `YES`, if the account is  *spam*  and `NO` otherwise.

You may print each character of the string in uppercase or lowercase. For example, the strings `YES`, `yes`, `Yes` and `yES` are identical.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X, Y \leq 100$
### Sample 1:
Input
Output

```
4
1 10
10 1
11 1
97 7

```

```
NO
NO
YES
YES

```

### Explanation:

 **Test case $1$:**  The following count is $1$ while the follower count is $10$. Since the following count is not more than $10$ times the follower count, the account is not spam.

 **Test case $2$:**  The following count is $10$ while the follower count is $1$. Since the following count is not  **more**  than $10$ times the follower count, the account is not spam.

 **Test case $3$:**  The following count is $11$ while the follower count is $1$. Since the following count is more than $10$ times the follower count, the account is spam.

 **Test case $4$:**  The following count is $97$ while the follower count is $7$. Since the following count is more than $10$ times the follower count, the account is spam.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T14:19:26.969Z  

```py
# cook your dish here
t = int(input())
for i  in range(t):
    x,y = map(int, input().split())
    if(x>10*y):
        print("yes")
    else:
        print("no")

```

---

[View on CodeChef](https://www.codechef.com/problems/INSTAGRAM)