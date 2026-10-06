# MVR - Rating 316

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Messi vs Ronaldo

In Chefland, a football player gets $2$ points for each goal and $1$ point for each assist.

Messi has $A$ goals and $B$ assists this season, whereas Ronaldo has $X$ goals and $Y$ assists.
Find out the player with more points this season.

### Input Format
- The first and only line of input will contains four space-separated integers $A$, $B$, $X$ and $Y$, the number of goals and assists that Messi has and the number of goals and assists that Ronaldo has, respectively.
### Output Format

Print a single line containing:

- Messi, if Messi has more points than Ronaldo.
- Ronaldo, if Ronaldo has more points than Messi.
- Equal, if both have equal points.

You can print each character in uppercase or lowercase. For example, the strings `Messi`, `MESSI`, `messi`, and `MeSSi` are considered identical.

### Constraints
- $0 \leq A,B,X,Y \leq 100$
### Sample 1:
Input
Output

```
40 30 50 10
```

```
Equal
```

### Explanation:
- Messi has $40$ goals and $30$ assists. Thus, his total points are $40\cdot 2+30 = 110$.
- Ronaldo has $50$ goals and $10$ assists. Thus, his total points are $50\cdot 2+10 = 110$.

Both have $110$ points.

### Sample 2:
Input
Output

```
91 22 60 30 
```

```
Messi
```

### Explanation:
- Messi has $91$ goals and $22$ assists. Thus, his total points are $91\cdot 2+22 = 204$.
- Ronaldo has $60$ goals and $30$ assists. Thus, his total points are $60\cdot 2+30 = 150$.

Messi has $204$ points, whereas Ronaldo has $150$.

### Sample 3:
Input
Output

```
60 30 80 20
```

```
Ronaldo
```

### Explanation:
- Messi has $60$ goals and $30$ assists. Thus, his total points are $60\cdot 2+30 = 150$.
- Ronaldo has $80$ goals and $20$ assists. Thus, his total points are $80\cdot 2+20 = 180$.

Messi has $150$ points, whereas Ronaldo has $180$.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-06T16:04:05.900Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int a,b,x,y;
	cin>>a>>b>>x>>y;
	if(((a*2)+b)>((2*x)+y)){
	    cout<<"messi";
	}
	else if(((a*2)+b)==((2*x)+y)){
	    cout<<"equal";
	}
	else{
	    cout<<"ronaldo";
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/MVR)