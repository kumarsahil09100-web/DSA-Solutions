# PRIZEPOOL - Rating 296

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Total Prize Money

In a coding contest, there are prizes for the top rankers. The prize scheme is as follows:

- Top $10$ participants receive rupees $X$ each.
- Participants with rank $11$ to $100$ (both inclusive) receive rupees $Y$ each.

Find the total prize money over all the contestants.

### Input Format
- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $X$ and $Y$ - the prize for top $10$ rankers and the prize for ranks $11$ to $100$ respectively.
### Output Format

For each test case, output the total prize money over all the contestants.

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq Y \leq X \leq 1000$
### Sample 1:
Input
Output

```
4
1000 100
1000 1000
80 1
400 30

```

```
19000
100000
890
6700

```

### Explanation:

 **Test Case $1$:**  Top $10$ participants receive rupees $1000$ and next $90$ participants receive rupees $100$ each. So, total prize money $= 10 \cdot 1000 + 90 \cdot 100 = 19000$.

 **Test Case $2$:**  Top $10$ participants receive rupees $1000$ and next $90$ participants receive rupees $1000$ each. So, total prize money $= 10 \cdot 1000 + 90 \cdot 1000 = 100000$.

 **Test Case $3$:**  Top $10$ participants receive rupees $80$ and next $90$ participants receive rupee $1$ each. So, total prize money $= 10 \cdot 80 + 90 \cdot 1 = 890$.

 **Test Case $4$:**  Top $10$ participants receive rupees $400$ and next $90$ participants receive rupees $30$ each. So, total prize money $= 10 \cdot 400 + 90 \cdot 30 = 6700$.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-03T16:39:33.237Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int x,y;
	    cin>>x>>y;
	    cout<<(x*10)+(y*90)<<endl;
	    
	    }

}

```

---

[View on CodeChef](https://www.codechef.com/problems/PRIZEPOOL)