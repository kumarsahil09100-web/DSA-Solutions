# PGNATK

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Pigeon Attack

Chef is tired of pigeons invading his balcony, and so decides to put up a net to keep them out.

It takes $N$ minutes of work to put up the net.
However, the pigeons won't leave Chef alone - every $K$-th minute, they'll fly onto the balcony and annoy Chef, leaving him unable to work.

That is, on minutes $K, 2K, 3K, \ldots$ Chef is unable to progress putting up the net.

How many minutes in total, including delays, will Chef need to finish putting up the net?

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input, containing two space-separated integers $N$ and $K$.
### Output Format

For each test case, output on a new line the total number of minutes needed for the net to be put up.

### Constraints
- $1 \leq T \leq 10^4$
- $1 \le N \le 100$
- $2 \le K \le 100$
### Sample 1:
Input
Output

```
4
3 2
5 3
4 10
7 4

```

```
5
7
4
9
```

### Explanation:

 **Test case $1$:**  Chef needs $N = 3$ minutes and the pigeons will show up every second minute, i.e. minutes $2, 4, 6, \ldots$

- Minute $1$: Chef will do some work.
- Minute $2$: Chef is unable to work due to pigeons.
- Minute $3$: Chef will do some work.
- Minute $4$: Chef is unable to work due to pigeons.
- Minute $5$: Chef will do some work. This is the third minute of work, so the net is put up. The answer is hence $5$.

 **Test case $2$:**  Chef needs $N = 5$ minutes and the pigeons will show up every third minute, i.e. minutes $3, 6, 9, \ldots$
Chef can work on minutes $1, 2, 4, 5, 7$ to put up the net; so the answer is $7$.

 **Test case $3$:**  Four minutes are needed, while the pigeons will show up every $10$-th minute. The net can be fully put up before the pigeons show up for the first time; needing only $4$ minutes.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T15:48:00.132Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here

}

```

---

[View on CodeChef](https://www.codechef.com/problems/PGNATK)