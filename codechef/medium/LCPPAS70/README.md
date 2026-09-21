# LCPPAS70

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program that takes three space separated numbers as input.

- Prints "Increasing" if the numbers are in strictly increasing order,
- "Decreasing" if they are in strictly decreasing order,
- and "Neither" otherwise.

Check the sample input / output below for further clarity.

### Sample 1:
Input
Output

```
20 30 41
```

```
Increasing
```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T18:16:58.365Z  

```c_cpp
 #include <iostream>
using namespace std;

int main() {
	// your code goes here
	int a,b,c;
	cin>>a>>b>>c;
	if(a<b &&b<c){
	    cout<<"increasing";
	}
	else  if (a>b && b>c){
	    cout<<"Decreasing";
	}
	else{
	    cout<<"Neither";
	}

}
```

---

[View on CodeChef](https://www.codechef.com/problems/LCPPAS70)