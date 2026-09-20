# DETSCORE - Rating 267

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Determine the Score

Chef appeared for a placement test.

There is a problem worth $X$ points. Chef finds out that the problem has exactly $10$ test cases. It is known that each test case is worth the same number of points.

Chef passes $N$ test cases among them. Determine the score Chef will get.

 **NOTE:**  See sample explanation for more clarity.

### Input Format
- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $X$ and $N$, the total points for the problem and the number of test cases which pass for Chef's solution.
### Output Format

For each test case, output the points scored by Chef.

### Constraints
- $1 \leq T \leq 100$
- $10 \leq X \leq 200$
- $0 \leq N \leq 10$
- $X$ is a multiple of $10$.
### Sample 1:
Input
Output

```
4
10 3
100 10
130 4
70 0

```

```
3
100
52
0

```

### Explanation:

 **Test Case $1$:**  The problem is worth $10$ points and since there are $10$ test cases, each test case is worth $1$ point. Since Chef passes $3$ test cases, his score will be $1 \cdot 3 = 3$ points.

 **Test Case $2$:**  The problem is worth $100$ points and since there are $10$ test cases, each test case is worth $10$ points. Since Chef passes all the $10$ test cases, his score will be $10 \cdot 10 = 100$ points.

 **Test Case $3$:**  The problem is worth $130$ points and since there are $10$ test cases, each test case is worth $13$ points. Since Chef passes $4$ test cases, his score will be $13 \cdot 4 = 52$ points.

 **Test Case $4$:**  The problem is worth $70$ points and since there are $10$ test cases, each test case is worth $7$ points. Since Chef passes $0$ test cases, his score will be $7 \cdot 0 = 0$ points.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-20T14:36:31.803Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int T;
	cin>>T;
	while(T--){
	    int X,N;
	    cin>>X>>N;
	    int y=X/10;
	    cout<<y*N<<endl;
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/DETSCORE)