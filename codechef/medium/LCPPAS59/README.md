# LCPPAS59

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program to check whether the given number as input is positive, negative, or zero.

### Sample 1:
Input
Output

```
20  
```

```
Positive  
```

### Sample 2:
Input
Output

```
0
```

```
Zero
```

### Sample 3:
Input
Output

```
-95
```

```
Negative
```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T18:13:13.188Z  

```c_cpp
#include <iostream>
using namespace std;

int main() {
    int num;
    cin>>num;
    if(num>0){
        cout<<"positive";
    }
    else if(num==0){
        cout<<"Zero";
    }
    else{
        cout<<"negative";
    }

    return 0;
}

```

---

[View on CodeChef](https://www.codechef.com/problems/LCPPAS59)