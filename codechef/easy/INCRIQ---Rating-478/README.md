# INCRIQ - Rating 478

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Increase IQ

A study has shown that playing a musical instrument helps in increasing one's IQ by $7$ points. Chef knows he can't beat Einstein in physics, but he wants to try to beat him in an IQ competition.

You know that Einstein had an IQ of $170$, and Chef currently has an IQ of $X$.

Determine if, after learning to play a musical instrument, Chef's IQ will become  **strictly greater than**  Einstein's.

Print "Yes" if it is possible for Chef to beat Einstein, else print "No" (without quotes).

You may print each character of the string in either uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes`, and `YES` will all be treated as identical).

### Input Format
- The first and only line of input will contain a single integer $X$, the current IQ of Chef.
### Output Format
- For each testcase, output in a single line "Yes" or "No"
- You may print each character of the string in either uppercase or lowercase (for example, the strings yEs, yes, Yes, and YES will all be treated as identical).
### Constraints
- $100 \leq X \leq 169$
### Subtasks

 **Subtask #1 (100 points):**  Original constraints

### Sample 1:
Input
Output

```
165
```

```
Yes
```

### Explanation:

After learning a musical instrument, Chef's final IQ will be $165+7=172$. Since $172 \gt 170$, Chef can beat Einstein.

### Sample 2:
Input
Output

```
120
```

```
No
```

### Explanation:

After learning a musical instrument, Chef's final IQ will be $120+7=127$. Since $127 \lt 170$, Chef cannot beat Einstein.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-21T13:43:50.371Z  

```py
# cook your dish here
x = int(input())
if(x+7>=170):
    print("yes")
else:
    print("no")
        
```

---

[View on CodeChef](https://www.codechef.com/problems/INCRIQ)