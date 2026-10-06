# FOURTICKETS - Rating 300

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-06T16:23:22.901Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int x,y;
	    cin>>x>>y;
	    if((y-x)>0){
	        cout<<"profit";
	    }
	    else if ((y-x)==0){
	        cout<<"neutral";
	    }
	    else{
	        cout<<"loss";
	    }
	    cout<<endl;
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/FOURTICKETS)