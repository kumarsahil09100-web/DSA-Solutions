# DSCTHR

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Score

Chef takes part in a discus throw competition, where each player gets  **three throws**. A player's final score is the  **longest distance**  achieved among their three throws.

Chef's throws cover distances of $A$, $B$, and $C$ units. Find his final score.

### Input Format
- The first line contains an integer $T$ — the number of test cases.
- Each test case contains three space-separated integers $A$, $B$, and $C$ — the distances of Chef's three throws.
### Output Format

For each test case, print Chef's final score on a separate line.

### Constraints
- $1 \le T \le 100$
- $1 \le A,B,C \le 100$
### Sample 1:
Input
Output

```
2
12 9 18
25 40 31
```

```
18
40
```

### Explanation:

 **Test case 1:**  The third throw covers the longest distance, $18$ units, so Chef's final score is $18$.

 **Test case 2:**  The second throw covers the longest distance, $40$ units, so Chef's final score is $40$.

### Sample 2:
Input
Output

```
2
24 24 24
50 17 50
```

```
24
50
```

### Explanation:

 **Test case 1:**  All three throws cover $24$ units, so Chef's final score is $24$.

 **Test case 2:**  The first and third throws both cover $50$ units, the longest distance. Chef's final score is $50$.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-12T15:00:50.966Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int a,b,c;
	    cin>>a>>b>>c;
	    if(a>b &&a>c){
	        
	        cout<<a;
	    }
	    else if(b>a && b>c){
	        cout<<b;
	    }
	    else{
	        cout<<c;
	    }
	    cout<<endl;
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/DSCTHR)