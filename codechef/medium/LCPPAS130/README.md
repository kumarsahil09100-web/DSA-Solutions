# LCPPAS130

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program that uses a for-each loop to print the square of each element in list of $N$ space separated integers, but skips elements greater than $10$.

Check the sample input and output below for further clarity.

 **Note** : Output the square of each element on a new line.

### Sample 1:
Input
Output

```
5
2 10 12 6 15
```

```
4
100
36
```

### Explanation:

Only 2, 10 and 6 are less or equal than 10, hence their squares are in output.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T18:41:34.822Z  

```c_cpp
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int N;
	cin>>N;
	int arr[N];
	for(int i=0;i<N;i++){
	    cin>>arr[i];
	}
	for(int i=0;i<N; i++){
	    if(arr[i]<=10){
	        cout<<arr[i]*arr[i]<<endl;
	    }
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/LCPPAS130)