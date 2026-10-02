# TALLER - Rating 281

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Who is taller!

Alice and Bob were having an argument about which of them is taller than the other. Charlie got irritated by the argument, and decided to settle the matter once and for all.

Charlie measured the heights of Alice and Bob, and got to know that Alice's height is $X$ centimeters and Bob's height is $Y$ centimeters. Help Charlie decide who is taller.

It is guaranteed that $X \neq Y$.

### Input Format
- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two integers $X$ and $Y$, as described in the problem statement.
### Output Format

For each test case, output on a new line $\texttt{A}$ if Alice is taller than Bob, else output $\texttt{B}$. The output is case insensitive, i.e, both $\texttt{A}$ and $\texttt{a}$ will be accepted as correct answers when Alice is taller.

### Constraints
- $1 \leq T \leq 1000$
- $100 \leq X, Y \leq 200$
- $X \neq Y$
### Sample 1:
Input
Output

```
2
150 160
160 150
```

```
B
A
```

### Explanation:

 **Test case $1$** : In this case, $150 < 160$ so Bob is taller than Alice.

 **Test case $2$** : In this case, $160 > 150$ so Alice is taller than Bob.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-02T16:03:31.920Z  

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
	        cout<<'A';
	    }
	    else{
	        cout<<'B';
	    }
	    cout<<endl;
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/TALLER)