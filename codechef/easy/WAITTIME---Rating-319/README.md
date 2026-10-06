# WAITTIME - Rating 319

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Waiting Time

Chef is eagerly waiting for a piece of information. His secret agent told him that this information would be revealed to him after $K$ weeks.

$X$ days have already passed and Chef is getting restless now. Find the number of  **remaining**  days Chef has to wait for, to get the information.

It is guaranteed that the information has not been revealed to the Chef yet.

### Input Format
- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $K$ and $X$, as described in the problem statement.
### Output Format

For each test case, output the number of remaining days that Chef will have to wait for.

### Constraints
- $1 \leq T \leq 500$
- $1 \leq K \leq 10$
- $1 \leq X \lt 7\cdot K$
### Sample 1:
Input
Output

```
4
1 5
1 6
1 1
1 2
```

```
2
1
6
5

```

### Explanation:

 **Test case $1$:**  The information will be revealed to the Chef after $1$ week, which is equivalent to $7$ days. Chef has already waited for $5$ days, so he needs to wait for $2$ more days in order to get the information.

 **Test case $2$:**  The information will be revealed to the Chef after $1$ week, which is equivalent to $7$ days. Chef has already waited for $6$ days, so he needs to wait for $1$ more day in order to get the information.

 **Test case $3$:**  The information will be revealed to the Chef after $1$ week, which is equivalent to $7$ days. Chef has already waited for $1$ day, so he needs to wait for $6$ more days in order to get the information.

 **Test case $4$:**  The information will be revealed to the Chef after $1$ week, which is equivalent to $7$ days. Chef has already waited for $2$ days, so he needs to wait for $5$ more days in order to get the information.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-06T16:19:37.391Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int k,x;
	    cin>>k>>x;
	    cout<<(k*7)-x<<endl;
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/WAITTIME)