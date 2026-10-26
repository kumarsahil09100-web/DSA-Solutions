# F1RULE - Rating 487

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Miami GP

Chef has finally got the chance of his lifetime to drive in the $F1$ tournament. But, there is one problem. Chef did not know about the 107% rule and now he is worried whether he will be allowed to race in the main event or not.

Given the fastest finish time as $X$ seconds and Chef's finish time as $Y$ seconds, determine whether Chef will be allowed to race in the main event or not.

Note that, Chef will only be allowed to race if his finish time is within  **107%**  of the fastest finish time.

### Input Format
- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, two space separated integers $X$ and $Y$ denoting the fastest finish time and Chef's finish time respectively.
### Output Format

For each test case, output $\texttt{YES}$ if Chef will be allowed to race in the main event, else output $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

### Constraints
- $1 \leq T \leq 2\cdot 10^4$
- $1 \leq X \leq Y \leq 200$
### Sample 1:
Input
Output

```
4
1 2
15 16
15 17
100 107

```

```
NO
YES
NO
YES

```

### Explanation:

 **Test case $1$:**  The fastest car finished in $1$ second. Thus, Chef should have finished on or before $1.07$ seconds to ensure qualification but he finished in $2$ seconds. Hence, Chef will not be allowed to race in the main event.

 **Test case $2$:**  The fastest car finished in $15$ seconds. Thus, Chef should have finished on or before $16.05$ seconds to ensure qualification and he managed to finish in $16$ seconds. Hence, Chef will be allowed to race in the main event.

 **Test case $3$:**  The fastest car finished in $15$ seconds. Thus, Chef should have finished on or before $16.05$ seconds to ensure qualification but he finished in $17$ seconds. Hence, Chef will not be allowed to race in the main event.

 **Test case $4$:**  The fastest car finished in $100$ seconds. Thus, Chef should have finished on or before $107$ seconds to ensure qualification and he finished just in time for qualification. Hence, Chef will be allowed to race in the main event.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-26T14:33:30.389Z  

```py
# cook your dish here
# cook your dish here
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if 100 * y <= 107 * x:
        print("YES")
    else:
        print("NO")


```

---

[View on CodeChef](https://www.codechef.com/problems/F1RULE)