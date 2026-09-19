# LUDO - Rating 260

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef Plays Ludo

Chef is playing Ludo. According to the rules of Ludo, a player can enter a new token into the play only when he rolls a $6$ on the die.

In the current turn, Chef rolled the number $X$ on the die. Determine if Chef can enter a new token into the play in the current turn or not.

### Input Format
- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains one integer $X$ — the number rolled by the Chef on the die.
### Output Format

For each test case, output `YES` if the Chef can enter a new token in the game. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

### Constraints
- $1 \le T \le 6$
- $1 \le X \le 6$
### Sample 1:
Input
Output

```
3
1
6
3

```

```
NO
YES
NO

```

### Explanation:

 **Test Case 1:**  Since Chef did not roll a $6$, he can not enter a new token in the play.

 **Test Case 2:**  Since Chef rolled a $6$, he can enter a new token in the play.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T15:46:12.813Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int T ;
	cin>>T;
	while(T--){
	    int X;
	    cin>>X;
	    if(X==6){
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

[View on CodeChef](https://www.codechef.com/problems/LUDO)