# LCPP20

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program to output the squares (using multiplication) of numbers from $1$ to $5$ on separate lines.

[ **Note:**  Please print in the same format as given below. There are single spaces between hyphen$(-)$ and digits.]

### Output Format

1 - 1
2 - 4
3 - 9
4 - 16
5 - 25

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T16:14:39.137Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	for(int i=1;i<=5;i++){
	    cout<<i<<"-"<<i*i<<endl;
	}


}

```

---

[View on CodeChef](https://www.codechef.com/problems/LCPP20)