# OFFBY1 - Rating 271

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Off By One

You just bought a new calculator, but it seems to have a small problem: all its results have an extra $1$ appended to the end.
For example, if you ask it for `3 + 5`, it'll print `81`, and `4 + 12` will result in `161`.

Given $A$ and $B$, can you predict what the calculator will print when you ask it for $A + B$?

### Input Format
- The first and only line of input will contain two space-separated integers $A$ and $B$.
### Output Format

Print a single integer: the calculator's output when you enter $A+B$ into it.

### Constraints
- $1 \leq A, B \leq 50$
### Sample 1:
Input
Output

```
3 5
```

```
81
```

### Explanation:

$3 + 5 = 8$, and the calculator appends a $1$ to print $81$.

### Sample 2:
Input
Output

```
4 12
```

```
161
```

### Explanation:

$4+12 = 16$, and the calculator appends a $1$ to print $161$.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-20T14:44:05.823Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int A,B;
	cin>>A>>B;
	cout<<A+B<<"1";

}

```

---

[View on CodeChef](https://www.codechef.com/problems/OFFBY1)