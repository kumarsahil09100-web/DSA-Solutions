# RIP2000 - Rating 284

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### 2000

Chef had collected $N$ notes of Rs. $2000$ to pay his total college fees. However, the government banned Rs. $2000$ notes.

Chef wants to pay the same amount using Rs. $500$ notes only. Find the number of notes Chef needs.

### Input Format

Each test case consists of a single integer $N$ - the number of notes of Rs. $2000$ that Chef has collected.

### Output Format

Output a single integer - the number of Rs. $500$ notes needed.

### Constraints
- $1 \leq N \leq 100$
### Sample 1:
Input
Output

```
4
```

```
16

```

### Explanation:

$4$ notes of Rs. $2000$ make a total of $4 \cdot 2000 = 8000$ rupees. This is equivalent to $16$ notes of Rs. $500$.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-02T16:11:45.638Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int n;
	cin>>n;
	cout<<4*n;

}

```

---

[View on CodeChef](https://www.codechef.com/problems/RIP2000)