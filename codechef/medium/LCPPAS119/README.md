# LCPPAS119

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program using a for loop to calculate the sum of the first $N$ natural numbers.

Check the sample input / output below for further details.

### Input Format
- The first and only line of input contain a positive integer $N$.
### Output Format
- Output on a single line, the sum of first $N$ natural numbers.
### Sample 1:
Input
Output

```
10
```

```
55
```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T18:34:51.115Z  

```c_cpp
#include <iostream>
using namespace std;

int main() {
    // Write your code here 
    int N;
    cin>>N;
    cout<<N*(N+1)/2;

    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/LCPPAS119)