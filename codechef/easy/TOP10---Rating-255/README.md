# TOP10 - Rating 255

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Masterchef finals

Chef has been working hard to compete in MasterChef.
He is ranked $X$ out of all contestants. However, only $10$ contestants would be selected for the finals.

Check whether Chef made it to the top $10$ or not?

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of one integers $X$ — the current rank of Chef.
### Output Format

For each test case, output on a new line, `YES`, if Chef made it to the top $10$ and `NO` otherwise.

Each character of the output may be printed in either uppercase or lowercase. That is, the strings `NO`, `no`, `nO`, and `No` will be treated as equivalent.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X \leq 100$
### Sample 1:
Input
Output

```
4
15
10
1
50
```

```
NO
YES
YES
NO
```

### Explanation:

 **Test case $1$:**  Chef's rank is $15$ which is greater than $10$. Thus, Chef did not make it to the top $10$.

 **Test case $2$:**  Chef's rank is $10$ which is equal to $10$. Thus, Chef made it to the top $10$.

 **Test case $3$:**  Chef made it to the top $10$, as his rank is $1$.

 **Test case $4$:**  Chef did not make it to the top $10$ as his rank is $50$.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-18T17:03:09.531Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int T;
	cin>>T;
	while(T--){
	    int X;
	    cin>>X;
	    if(X<=10){
	        cout<<"yes";
	    }
	    else{
	        cout<<"NO";
	    }
	    cout<<endl;
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/TOP10)