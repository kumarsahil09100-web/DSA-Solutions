# FOURTICKETS - Rating 302

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Four Tickets

Four friends want to attend a concert. Each ticket costs $X$ rupees.
They have decided to go to the concert if and only if the total cost of the tickets does  **not exceed**  $1000$ rupees.

Determine whether they will be going to the concert or not.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $X$, the cost of each ticket.
### Output Format

For each test case, output `YES` if they will be going to the concert, `NO` otherwise.

You can print each character in uppercase or lowercase. For example, the strings `YES`, `yes`, `Yes`, and `yES`, are all considered identical.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X \leq 1000$
### Sample 1:
Input
Output

```
4
100
500
250
1000
```

```
YES
NO
YES
NO

```

### Explanation:

 **Test case $1$:**  The total cost of all tickets is $100\cdot 4 = 400$ which is $\le 1000$. Thus, they will go to the concert.

 **Test case $2$:**  The total cost of all tickets is $500\cdot 4 = 2000$ which is $\gt 1000$. Thus, they will not go to the concert.

 **Test case $3$:**  The total cost of all tickets is $250\cdot 4 = 1000$ which is $\le 1000$. Thus, they will go to the concert.

 **Test case $4$:**  The total cost of all tickets is $1000\cdot 4 = 4000$ which is $\gt 1000$. Thus, they will not go to the concert.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-05T15:04:50.170Z  

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
	    if((4*x)>1000){
	        cout<<"no";
	        
	    }
	    else{
	        cout<<"yes";
	    }
	    cout<<endl;
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/FOURTICKETS)