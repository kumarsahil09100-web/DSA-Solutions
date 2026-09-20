# ERROR404 - Rating 267

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### 404 Not Found

Chef's website has a specific response mechanism based on the HTTP status code received:

- If the response code is $404$, the website will return NOT FOUND.
- For any other response code different from $404$, the website will return FOUND.

Given the response code as $X$, determine the website response.

### Input Format
- The first and only line of input contains a response code $X$.
### Output Format

Output on a new line `NOT FOUND`, if the response code is $404$. Otherwise print `FOUND`.

You may print each character of the string in uppercase or lowercase (for example, the strings `FOUND`, `fouND`, `FouND`, and `found` will all be treated as identical).

### Constraints
- $100 \leq X \leq 999$
### Sample 1:
Input
Output

```
200

```

```
FOUND
```

### Explanation:

Since the response code is not $404$, website returns `FOUND`.

### Sample 2:
Input
Output

```
404

```

```
NOT FOUND
```

### Explanation:

Since the response code is $404$, website returns `NOT FOUND`.

### Sample 3:
Input
Output

```
301

```

```
FOUND
```

### Explanation:

Since the response code is not $404$, website returns `FOUND`.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-20T14:39:46.113Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int X;
	cin>>X;
	if(X==404){
	    cout<<"NOT FOUND";
	}
	else{
	    cout<<"FOUND";
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/ERROR404)