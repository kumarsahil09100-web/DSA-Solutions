# MANAPTS - Rating 327

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Mana Points

Chef is playing a mobile game. In the game, Chef's character  *Chefario*  can perform special attacks. However, one special attack costs $X$ mana points to Chefario.

If Chefario currently has $Y$ mana points, determine the  **maximum**  number of special attacks he can perform.

### Input Format
- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space-separated integers $X$ and $Y$ — the cost of one special attack and the number of mana points Chefario has initially.
### Output Format

For each test case, output the maximum number of special attacks Chefario can perform.

### Constraints
- $1 \leq T \leq 10^5$
- $1 \le X \le 100$
- $1 \le Y \le 1000$
### Sample 1:
Input
Output

```
3
10 30
6 41
50 2

```

```
3
6
0

```

### Explanation:

 **Test case $1$:**  Chefario can perform a maximum of $3$ special attacks which will cost him $30$ mana points.

 **Test case $2$:**  Chefario can perform a maximum of $6$ special attacks which will cost him $36$ mana points. Note that Chefario can not perform $7$ special attacks as these will cost him $42$ mana points while he has only $41$ mana points.

 **Test case $3$:**  Chefario will not be able to perform any special attacks in this case.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-08T13:09:25.138Z  

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
        cout<<y/x<<endl;
    }

}

```

---

[View on CodeChef](https://www.codechef.com/problems/MANAPTS)