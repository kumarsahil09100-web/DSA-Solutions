# BESTOFTWO - Rating 284

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Best of Two

Chef took an examination two times. In the first attempt, he scored $X$ marks while in the second attempt he scored $Y$ marks. According to the rules of the examination, the best score out of the two attempts will be considered as the final score.

Determine the final score of the Chef.

### Input Format
- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $X$ and $Y$ — the marks scored by Chef in the first attempt and second attempt respectively.
### Output Format

For each test case, output the final score of Chef in the examination.

### Constraints
- $1 \leq T \leq 1000$
- $0 \le X, Y \le 100$
### Sample 1:
Input
Output

```
4
40 60
67 55
50 50
1 100

```

```
60
67
50
100

```

### Explanation:

 **Test Case 1:**  The best score out of the two attempts is $60$.

 **Test Case 2:**  The best score out of the two attempts is $67$.

 **Test Case 3:**  The best score out of the two attempts is $50$.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-02T16:09:02.944Z  

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
	    if(x>y){
	        cout<<x;
	    }
	        else {
	            cout<<y;
	        }
	        cout<<endl;
	    
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/BESTOFTWO)