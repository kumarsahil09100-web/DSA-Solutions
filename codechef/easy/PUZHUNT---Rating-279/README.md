# PUZHUNT - Rating 279

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Puzzle Hunt

Chef and some of his friends are planning to participate in a puzzle hunt event.

The rules of the puzzle hunt state:
"This hunt is intended for teams of $6$ to $8$ people."

Chef's team has $N$ people in total. Are they eligible to participate?

### Input Format

The first and only line of input will contain a single integer $N$: the number of people present in Chef's team.

### Output Format

Print the answer: `Yes` if Chef's team is eligible to participate, and `No` otherwise.

Each letter in the output may be printed in either uppercase or lowercase, i.e, the outputs `NO`, `No`, `nO`, `no` will all be treated as equivalent.

### Constraints
- $1 \leq N \leq 10$
### Sample 1:
Input
Output

```
4
```

```
No
```

### Explanation:

The puzzle hunt requires between $6$ and $8$ people in a team.
$4$ isn't between $6$ and $8$, so Chef's team cannot participate.

### Sample 2:
Input
Output

```
7
```

```
Yes
```

### Explanation:

Chef's team has $7$ people, and $7$ lies between $6$ and $8$.
So, Chef's team can participate in the event.

### Sample 3:
Input
Output

```
8

```

```
Yes
```

### Explanation:

Chef's team has $8$ people, and $8$ lies between $6$ and $8$.
So, Chef's team can participate in the event.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-02T15:54:30.196Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int n;
	cin>>n;
	if(n>=6&&n<=8){
	    cout<<"yes";
	}
	else{
	    cout<<"no";
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/PUZHUNT)