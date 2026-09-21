# LCPPAS139

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a function named  **calculatePower**  that takes two integer,  **base**  and  **exponent**  respectively, and returns the result of raising  **base**  to the power of  **exponent**.

### Sample 1:
Input
Output

```
2 3
```

```
8
```

### Explanation:

23 = 8

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T18:46:26.700Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int calculatePower(int base, int exponent) {
    // Complete the function
    return pow(base,exponent)  ;
    
}

int main() {
    int base, exponent;
    cin >> base >> exponent;
    int result = calculatePower(base, exponent);
    cout << result;

    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/LCPPAS139)