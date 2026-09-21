# LCPPAS90

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Rectify the errors in the program to get the desired output.

Check the sample input / output below for further clarity.

### Sample 1:
Input
Output

```
1
```

```
Option 1 selected
```

### Sample 2:
Input
Output

```
2
```

```
Option 2 selected
```

### Sample 3:
Input
Output

```
3
```

```
Option 3 selected
```

### Sample 4:
Input
Output

```
Any number other than 1, 2 or 3
```

```
Invalid choice
```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T18:26:00.760Z  

```c_cpp
#include <iostream>
using namespace std;
int main() {
    int choice;
    cin >> choice;
    switch(choice) {
        case 1:
            cout << "Option 1 selected";
            break;
        case 2:
            cout << "Option 2 selected";
            break;
        case 3:
            cout << "Option 3 selected";
            break;
        default:
            cout << "Invalid choice";
    }

    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/LCPPAS90)