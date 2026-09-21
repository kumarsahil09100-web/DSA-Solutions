# LCPPAS40

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program to print the length of each word of the sentence given below as well as the length of the whole sentence.
 **"Coding on CodeChef"** 

[ **Note:**  Don't forget to print the outputs in same format as given below.]

### Sample 1:
Input
Output

```

```

```
Coding - 6  
on - 2  
CodeChef - 8  
Coding on CodeChef - 18  
```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T18:09:25.168Z  

```c_cpp
#include <iostream>
using namespace std;

int main() {
    string one = "Coding";
    string two = "on";
    string three = "CodeChef";
    // Write your code below
    string four = one+" "+two+" "+three;
cout<<one <<"-"<<one.size()<<endl;
cout<<two<<"-"<<two.size()<<endl;
cout<<three<<"-"<<three.size()<<endl;
cout<<four<<"-"<<four.size();



    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/LCPPAS40)