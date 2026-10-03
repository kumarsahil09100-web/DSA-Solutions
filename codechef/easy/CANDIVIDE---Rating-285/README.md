# CANDIVIDE - Rating 285

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Roller Coaster

Chef's son wants to go on a roller coaster ride. The height of Chef's son is $X$ inches while the  **minimum**  height required to go on the ride is $H$ inches. Determine whether he can go on the ride or not.

### Input Format
- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $X$ and $H$ - the height of Chef's son and the minimum height required for the ride respectively.
### Output Format

For each test case, output in a single line, `YES` if Chef's son can go on the ride. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical)

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq X, H \leq 100$
### Sample 1:
Input
Output

```
4
15 20
50 48
32 32
38 39

```

```
NO
YES
YES
NO
```

### Explanation:

 **Test case 1:**  Chef's son can not go on the ride as his height $\lt$ the minimum required height.

 **Test case 2:**  Chef's son can go on the ride as his height $\ge$ the minimum required height.

 **Test case 3:**  Chef's son can go on the ride as his height $\ge$ the minimum required height.

 **Test case 4:**  Chef's son can not go on the ride as his height $\lt$ the minimum required height.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-03T16:17:46.539Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
while(t--){
    int x,h;
	cin>>x>>h;
	if(x>=h){
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