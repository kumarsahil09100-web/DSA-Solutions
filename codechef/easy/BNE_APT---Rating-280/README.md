# BNE_APT - Rating 280

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Bone Appetit

 *Trick or treat, bags of sweets, ghosts are walking down the street* 

It's Halloween and Suri Bhai is out to get his treats.
There are two sectors in his neighborhood, "Bones" and "Blood". They have $N$ and $M$ people, respectively.

Each person in "Bones" will hand out $X$ treats, and each person in "Blood" will hand out $Y$ treats.
How many treats does Suri Bhai get from visiting everyone in his neighborhood in total?

### Input Format
- The first line of input contains two space-separated integers $N$ and $M$ — the number of people in "Bones" and "Blood", respectively.
- The second line of input contains two space-separated integers $X$ and $Y$ — the number of treats handed out by each person in "Bones" and "Blood", respectively.
### Output Format

For each test case output a single integer: the total number of treats Suri Bhai will receive.

### Constraints
- $0 \leq N,M \leq 100$
- $0 \leq X,Y \leq 1000$
### Sample 1:
Input
Output

```
4 2
5 6

```

```
32

```

### Explanation:
- "Bones" has $4$ people, each of who will give out $5$ treats, for a total of $4\times 5 = 20$ treats.
- "Blood" has $2$ people, each of who will give out $6$ treats, for a total of $2\times 6 = 12$ treats.
- The total number of treats is $20 + 12 = 32$.
### Sample 2:
Input
Output

```
5 0
0 2

```

```
0

```

### Explanation:
- "Bones" has $5$ people, each of who will give out $0$ treats, for a total of $5\times 0 = 0$ treats.
- "Blood" has $0$ people, each of who will give out $2$ treats, for a total of $0\times 2 = 0$ treats.
- The total number of treats is $0 + 0 = 0$.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-02T15:58:59.114Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int n,m;
	cin>>n>>m;
	int x,y;
	cin>>x>>y;
	cout<<(n*x)+(m*y);

}

```

---

[View on CodeChef](https://www.codechef.com/problems/BNE_APT)