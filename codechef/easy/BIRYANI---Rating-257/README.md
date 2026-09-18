# BIRYANI - Rating 257

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Biryani classes

According to a recent survey, Biryani is the most ordered food. Chef wants to learn how to make world-class Biryani from a MasterChef. Chef will be required to attend the MasterChef's classes for $X$ weeks, and the cost of classes per week is $Y$ coins. What is the total amount of money that Chef will have to pay?

### Input Format
- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $X$ and $Y$, as described in the problem statement.
### Output Format

For each test case, output on a new line the total amount of money that Chef will have to pay.

### Constraints
- $1 \leq T \leq 10^4$
- $1 \leq X, Y \leq 100$
### Sample 1:
Input
Output

```
4
1 10
1 15
2 10
2 15
```

```
10
15
20
30

```

### Explanation:

 **Test case $1$:**  Chef will be required to attend the MasterChef's classes for $1$ week and the cost of classes per week is $10$ coins. Hence, Chef will have to pay $10$ coins in total.

 **Test case $2$:**  Chef will be required to attend the MasterChef's classes for $1$ week and the cost of classes per week is $15$ coins. Hence, Chef will have to pay $15$ coins in total.

 **Test case $3$:**  Chef will be required to attend the MasterChef's classes for $2$ weeks and the cost of classes per week is $10$ coins. Hence, Chef will have to pay $20$ coins in total.

 **Test case $4$:**  Chef will be required to attend the MasterChef's classes for $2$ weeks and the cost of classes per week is $15$ coins. Hence, Chef will have to pay $30$ coins in total.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-18T17:09:21.334Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int T;
	cin>>T;
	while(T--){
	    int X,Y;
	    cin>>X>>Y;
	    cout<<X*Y<<endl;
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/BIRYANI)