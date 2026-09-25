# KITCHENTIME - Rating 273

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Kitchen Timings

The working hours of Chef’s kitchen are from $X$ pm to $Y$ pm $(1 \le X \lt Y \le 12)$.

Find the number of hours Chef works.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $X$ and $Y$ — the starting and ending time of working hours respectively.
### Output Format

For each test case, output on a new line, the number of hours Chef works.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X \lt Y \leq 12$
### Sample 1:
Input
Output

```
4
1 2
3 7
9 11
2 10

```

```
1
4
2
8

```

### Explanation:

 **Test case $1$:**  Chef starts working at $1$ pm and works till $2$ pm. Thus, he works for $1$ hour.

 **Test case $2$:**  Chef starts working at $3$ pm and works till $7$ pm. Thus, he works for $4$ hours.

 **Test case $3$:**  Chef starts working at $9$ pm and works till $11$ pm. Thus, he works for $2$ hours.

 **Test case $4$:**  Chef starts working at $2$ pm and works till $10$ pm. Thus, he works for $8$ hours.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-25T15:55:20.967Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int T;
	cin>> T;
	while(T--){
	    int X,Y;
	    cin>>X>>Y;
	    cout<<Y-X<<endl;
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/KITCHENTIME)