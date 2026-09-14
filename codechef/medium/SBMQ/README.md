# SBMQ

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Subtree Maximum Queries

You are given a rooted tree consisting of $N$ nodes,  **rooted at node $1$**.

The tree is represented by the array $parent$, where $parent[i]$ denotes the parent of node $i$, and $parent[1]=0$.

Each node has a value assigned to it, represented by the array $value$, where $value[i]$ denotes the value of node $i$.

You are given $Q$ operations. Each operation is one of the following types:

- $1\ u\ x$: Update the value of node $u$ by setting $value[u]=x$.
- $2\ u$: Print the maximum value among all nodes in the subtree rooted at node $u$.

Process the operations  **in the order they are given**. Each query uses the values after all preceding updates.

The subtree of a node  **includes the node itself**.

### Input Format
- The first line contains an integer $N$ — the number of nodes.
- The second line contains $N$ space-separated integers representing the array $parent$.
- The third line contains $N$ space-separated integers representing the array $value$.
- The fourth line contains an integer $Q$ — the number of operations.
- Each of the next $Q$ lines contains one of the following: $1\ u\ x$, representing an update operation. $2\ u$, representing a subtree maximum query.
### Output Format

For each operation of type $2$, print a single integer — the  **maximum value among all nodes in the subtree rooted at node $u$**.

Print each answer on a separate line.

Do not print anything for operations of type $1$.

### Constraints
- $1 \le N,Q \le 2 \times 10^5$
- $parent[1]=0$
- $1 \le parent[i] \le N$ for $2 \le i \le N$
- The array $parent$ represents a valid tree rooted at node $1$.
- $0 \le value[i] \le 10^9$
- $1 \le u \le N$
- $0 \le x \le 10^9$
### Sample 1:
Input
Output

```
4
0 1 1 3
5 3 7 2
4
2 1
2 3
1 4 10
2 3
```

```
7
7
10
```

### Explanation:

The given arrays are:

- $parent=[0,1,1,3]$
- $value=[5,3,7,2]$

For the first operation, the subtree rooted at node $1$ contains nodes $\{1,2,3,4\}$. The maximum value in this subtree is $7$.

For the second operation, the subtree rooted at node $3$ contains nodes $\{3,4\}$. Their values are $[7,2]$, so the maximum value is $7$.

For the third operation, set $value[4]=10$. The array becomes:

$$ value=[5,3,7,10] $$

For the fourth operation, the values in the subtree rooted at node $3$ are now $[7,10]$, so the maximum value is $10$.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-14T15:15:29.588Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here

}

```

---

[View on CodeChef](https://www.codechef.com/problems/SBMQ)