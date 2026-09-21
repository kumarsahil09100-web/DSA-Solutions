# LCPPAS71

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T18:16:59.764Z  

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

[View on CodeChef](https://www.codechef.com/problems/LCPPAS71)