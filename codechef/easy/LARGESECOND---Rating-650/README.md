# LARGESECOND - Rating 650

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-31T17:05:44.532Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int N;
	    cin>>N;
	    vector<long long> A(N);
	    for(int i=0;i<N;i++){
	        cin>>A[i];
	    }
	    long long tall=A[0];
	    for(int i=1;i<N;i++){
	        if(A[i]>tall){
	            tall=A[i];
	        }
	    
	    }
	    cout<<tall<<endl;
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/LARGESECOND)