# HUNDW

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Houses Under Watch

A street has $100$ houses, numbered $1$ through $100$ from left to right. Cops are stationed at $M$ distinct houses, given by $A_1,A_2,\ldots,A_M$.

Each cop can travel up to $X$ house positions per minute and has $Y$ minutes to search. Therefore, a house numbered $H$ is  **within reach**  of a cop at house $A_i$ if $|H-A_i|\le X\times Y$. The cop's own house is also within reach.

Devu wants to hide in a house that is  **outside the reach of every cop**. Find the number of such houses.

### Input Format

The first line contains an integer $T$ — the number of test cases.

- For each test case: The first line contains three space-separated integers $M$, $X$, and $Y$. The second line contains $M$ space-separated integers $A_1,A_2,\ldots,A_M$ — the houses where cops are stationed.
### Output Format

For each test case, print the number of safe houses on a separate line.

### Constraints
- $1 \le T \le 10^4$
- $1 \le M,X,Y \le 10$
- $1 \le A_i \le 100$
- All $A_i$ are distinct.
### Sample 1:
Input
Output

```
2
2 2 5
20 35
1 3 4
5
```

```
64
83
```

### Explanation:

 **Test case 1:**  Each cop can travel up to $10$ house positions. The cops can reach houses $10$ through $30$ and $25$ through $45$, respectively. Together, these ranges cover $36$ houses, so $100-36=64$ houses are safe.

 **Test case 2:**  The cop can travel up to $12$ house positions. Within the street, houses $1$ through $17$ are within reach. The remaining $100-17=83$ houses are safe.

### Sample 2:
Input
Output

```
1
1 10 5
50
```

```
0
```

### Explanation:

 **Test case 1:**  The cop can travel up to $50$ house positions from house $50$, placing every house from $1$ through $100$ within reach. No house is safe.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-12T15:14:18.653Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here

}

```

---

[View on CodeChef](https://www.codechef.com/problems/HUNDW)