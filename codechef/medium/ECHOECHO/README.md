# ECHOECHO

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Echo

A string of length $4$ is called an  *echo*  if $S_1 = S_3$ and $S_2 = S_4$.
Here, we are using $1$-indexing.

You are given a string of length $4$. Check if it is an  *echo*.

### Input Format
- The first and only line of input will contain a single string $S$ of length $4$.
### Output Format

Print `Yes` if $S$ is an  *echo*, and `No` otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e. the strings `NO`, `No`, `nO`, and `no` will be treated as equivalent.

### Constraints
- $S$ has length $4$.
- $S$ consists of only lowercase English letters, i.e. the characters a, b, c,..., z.
### Sample 1:
Input
Output

```
meme

```

```
Yes

```

### Explanation:

The first and third characters of `meme` are both equal (to `m`), and its second and fourth characters are also both equal (to `e`).
So, `meme` is an  *echo*.

### Sample 2:
Input
Output

```
ever

```

```
No
```

### Explanation:

The second character of `ever` is `v`, while its fourth character is `r`. These are not equal, so `ever` is not an  *echo*.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T15:45:55.699Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here

	string s[4];
    for(int i=0;i<4;i++){
        cin>>s[i];
    }
	}
	if(s[0]==s[2] && s[1]==s[3]){
	    cout<<"yes";
	}
	else{
	    cout<<"no";
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/ECHOECHO)