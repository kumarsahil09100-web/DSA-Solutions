# LCPPAS99

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program to declare and accept an array / list of $N$ space separate integers.
Calculate the  **multiplication**  of the 1st and 3rd elements of the array and output the same to the console.

Check the sample input / output below for further clarity.

### Sample 1:
Input
Output

```
5
10 12 25 9 20
```

```
250
```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T18:30:04.197Z  

```c_cpp
#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    int arr[N];
    // update your code below this line
    for(int i=0;i<N;i++){
        cin>>arr[i];
    }
    cout<<arr[0]*arr[2];
    
    

    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/LCPPAS99)