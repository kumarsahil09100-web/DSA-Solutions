# BALASUB

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### SuBalance

An array $B$ is called  *balanced*  if it has an equal number of prefix maximums and suffix maximums.
Here,

- Element $B_i$ is a prefix maximum if $B_i \ge B_j$ for all $1 \le j \lt i$
- Element $B_i$ is a suffix maximum if $B_i \ge B_j$ for all $i \lt j \le |B|$, where $|B|$ denotes the length of $B$.

You are given an array $A$ of length $N$.

Find  *any*  contiguous subarray of $A$ with  **length at least $2$**  that's balanced, i.e. find any pair $(L, R)$ such that $1 \le L \lt R \le N$ and $[A_L, \ldots, A_R]$ is balanced.

If there are multiple balanced subarrays of $A$ of length $\ge 2$, you may find any of them.
If there are no balanced subarrays in $A$ of length $\ge 2$, print $-1$.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input. The first line of each test case contains a single integers $N$ — the length of the array. The second line contains $N$ space-separated integers $A_1, \ldots, A_N$.
### Output Format

For each test case, on a new line:

- If no balanced subarray of length $\ge 2$ exists, print the single integer $-1$.
- Otherwise, print two space-separated integers $L$ and $R$ ($1 \le L \lt R \le N$), denoting that the subarray $[A_L, \ldots, A_R]$ is balanced.

If there are multiple balanced subarrays of length $\ge 2$, you may find any one of them.

### Constraints
- $1 \leq T \leq 10^5$
- $2 \leq N \leq 2\cdot 10^5$
- $1 \le A_i \le N$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.
### Sample 1:
Input
Output

```
5
2
1 2
3
1 3 2
4
3 1 1 3
5
5 3 1 2 4
5
5 1 5 3 4

```

```
-1
1 3
1 4
-1
2 5
```

### Explanation:

 **Test case $1$:**  The only subarray of length $\ge 2$ is $[1, 2]$, which is not balanced because it has two prefix maximums but only one suffix maximum.
So, we output $-1$.

 **Test case $2$:**  The subarray $[1, 3, 2]$ is balanced, having two prefix maximums ($1$ and $3$) as well as two suffix maximums ($2$ and $3$).

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-09T15:58:50.238Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;

        string A, B;
        cin >> A;
        cin >> B;

        int countA = 0;
        int countB = 0;

        // Count 'a' in A
        for (int i = 0; i < N; i++) {
            if (A[i] == 'a') {
                countA++;
            }
        }

        // Count 'a' in B
        for (int i = 0; i < N; i++) {
            if (B[i] == 'a') {
                countB++;
            }
        }

        // For every position, characters must be different
        if (countA + countB == N) {
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }

    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/BALASUB)