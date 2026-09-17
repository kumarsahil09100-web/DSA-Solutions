# CWC23QUALIF - Rating 203

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Cricket World Cup Qualifier

The cricket World Cup has started in Chefland. There are many teams participating in the group stage matches. Any team that scores $12$ or more points in the group stage matches qualifies for the next stage.

You know the score that a particular team has scored in the group stage matches. Determine if the team has qualified for the next stage or not.

### Input Format

The first and only line of input consists of an integer $X$ denoting the total points scored by the given team in the group stage matches.

### Output Format

Output `Yes`, if the team has qualified for the next stage, and `No` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

### Constraints
- $1 \leq X \leq 20$
### Sample 1:
Input
Output

```
3

```

```
No

```

### Explanation:

The team has not scored $\ge 12$ points. Hence it does not qualify.

### Sample 2:
Input
Output

```
17

```

```
Yes

```

### Explanation:

The team has scored $\ge 12$ points. Hence it does qualify.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-17T15:41:20.174Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	int X;
	cin>>X;
	if(X>=12){
	    cout<<"yes";
	}
	else{
	    cout<<"No";
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/CWC23QUALIF)