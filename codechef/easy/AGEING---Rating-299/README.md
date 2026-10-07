# AGEING - Rating 299

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Ageing

Chef's current age is $20$ years, while Chefina's current age is $10$ years.
Determine Chefina's age when Chef will be $X$ years old.

Note: Assume that Chef and Chefina were born on same day and same month (just different year).

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $X$, the age of Chef.
### Output Format

For each test case, output Chefina's age when Chef will be $X$ years old.

### Constraints
- $1 \leq T \leq 25$
- $25 \leq X \leq 50$
### Sample 1:
Input
Output

```
4
25
36
50
44

```

```
15
26
40
34

```

### Explanation:

 **Test case $1$:**  Chefina is $10$ years old when Chef is $20$ years old. Thus, when Chef would be $25$, Chefina would be $15$.

 **Test case $2$:**  Chefina is $10$ years old when Chef is $20$ years old. Thus, when Chef would be $36$, Chefina would be $26$.

 **Test case $3$:**  Chefina is $10$ years old when Chef is $20$ years old. Thus, when Chef would be $50$, Chefina would be $40$.

 **Test case $4$:**  Chefina is $10$ years old when Chef is $20$ years old. Thus, when Chef would be $44$, Chefina would be $34$.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-07T15:43:36.082Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int x;
	    cin>>x;
	    cout<<x-10<<endl;
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/AGEING)