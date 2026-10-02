# CANDIVIDE - Rating 289

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Candy Division

There are  **three**  friends and a total of $N$ candies.
There will be a fight amongst the friends if all of them do  **not**  get the same number of candies.

Chef wants to divide  **all**  the candies such that there is  **no fight**. Find whether such distribution is possible.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $N$ - the number of candies.
### Output Format

For each test case, output `YES`, if we can distribute all the candies between the three friends equally. Otherwise output `NO`.

You can output each character of the answer in uppercase or lowercase. For example, the strings `yEs`, `yes`, `Yes`, and YES are considered the same.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
### Sample 1:
Input
Output

```
4
3
4
2
6

```

```
YES
NO
NO
YES
```

### Explanation:

 **Test case $1$:**  Chef can distribute all $3$ candies such that each friend gets $1$ candy. Since all three friends have same number of candies, there is no fight.

 **Test case $2$:**  There exist no way of distributing  **all**  candies such that all three friends have same number of candies.

 **Test case $3$:**  There exist no way of distributing  **all**  candies such that all three friends have same number of candies.

 **Test case $4$:**  Chef can distribute all $6$ candies such that each friend gets $2$ candies. Since all three friends have same number of candies, there is no fight.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-02T16:35:49.366Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    if(n%3==0){
	        cout<<"yes";
	        
	    }
	    else{
	        cout<<"no";
	    }
	    cout<<endl;
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/CANDIVIDE)