# DNATION - Rating 305

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef and Donation

In a certain month, Chef earned $X$ rupees while Chefina earned $Y$ rupees such that $Y\gt X$.
Since they want to end up with  **exactly**  the same amount, they decide to donate the difference between their income to a charity.

Find the amount they donate in the month.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $X$ and $Y$ — the income of Chef and Chefina in a month, respectively.
### Output Format

For each test case, output on a new line, the amount they donate in the month.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X\lt Y \leq 10$
### Sample 1:
Input
Output

```
4
1 3
2 5
4 5
2 10

```

```
2
3
1
8

```

### Explanation:

 **Test case $1$:**  Chef earns $1$ rupees while Chefina earns $3$ rupees. The difference between their income is $3-1 = 2$. Thus, they donate $2$ rupees to charity.

 **Test case $2$:**  Chef earns $2$ rupees while Chefina earns $5$ rupees. The difference between their income is $5-2 = 3$. Thus, they donate $3$ rupees to charity.

 **Test case $3$:**  Chef earns $4$ rupees while Chefina earns $5$ rupees. The difference between their income is $5-4 = 1$. Thus, they donate $1$ rupees to charity.

 **Test case $4$:**  Chef earns $2$ rupees while Chefina earns $10$ rupees. The difference between their income is $10-2 = 8$. Thus, they donate $8$ rupees to charity.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-06T16:23:48.363Z  

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
	    cout<<y-x<<endl;
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/DNATION)