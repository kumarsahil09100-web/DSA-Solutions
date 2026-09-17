# LUCKYSEVEN - Rating 213

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Lucky Seven

Chef considers the number $7$ lucky. As a result, he believes that the $7$-th letter he sees on a day is his  *lucky letter*  of the day.

You are given a string $S$ of length $10$, denoting the first $10$ letters Chef saw today.
What is Chef's  *lucky letter* ?

### Input Format
- The only line of input contains a string $S$, of length $10$.
### Output Format
- Print a single character: Chef's lucky letter.
### Constraints
- $S$ has a length of $10$
- $S$ contains only lowercase Latin letters (i.e, the characters 'a' to 'z')
### Sample 1:
Input
Output

```
proceeding
```

```
d
```

### Explanation:

The $7$-th character of $\texttt{"proceeding"}$ is `'d'`, and hence that is Chef's lucky letter.

### Sample 2:
Input
Output

```
outofsight
```

```
i
```

### Explanation:

The $7$-th character of $\texttt{"outofsight"}$ is `'i'`, and hence that is Chef's lucky letter.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-17T15:49:02.193Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
    string s;
    cin>>s;
    cout<<s[6];

}

```

---

[View on CodeChef](https://www.codechef.com/problems/LUCKYSEVEN)