# TAXSAVING - Rating 252

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Saving Taxes

In Chefland, everyone who earns  **strictly**  more than $Y$ rupees per year, has to pay a tax to Chef. Chef has allowed a special scheme where you can invest any amount of money and claim exemption for it.

You have earned $X$ $(X \gt Y)$ rupees this year. Find the  **minimum**  amount of money you have to invest so that you don't have to pay taxes this year.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input consisting of two space separated integers $X$ and $Y$ denoting the amount you earned and the amount above which you will have to pay taxes.
### Output Format

For each test case, output a single integer, denoting the minimum amount you need to invest.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq Y \lt X \leq 100$
### Sample 1:
Input
Output

```
4
4 2
8 7
5 1
2 1

```

```
2
1
4
1

```

### Explanation:

 **Test case $1$:**  The amount above which you will have to pay taxes is $2$. Since you earn $4$ rupees, you need to invest at least $2$ rupees. After investing $2$ rupees, you will remain with an effective income $4 - 2 = 2$ rupees which will not be taxed.

 **Test case $2$:**  The amount above which you will have to pay taxes is $7$. Since you earn $8$ rupees, you need to invest at least $1$ rupees.

 **Test case $3$:**  The amount above which you will have to pay taxes is $1$. Since you earn $5$ rupees, you need to invest at least $4$ rupees.

 **Test case $4$:**  The amount above which you will have to pay taxes is $1$. Since you earn $2$ rupees, you need to invest at least $1$ rupees.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-18T16:59:03.805Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int T;
	cin>>T;
	while(T--){
	    int X,Y;
	    cin>>X>>Y;
	   cout<<X-Y<<endl;
	}

}

```

---

[View on CodeChef](https://www.codechef.com/problems/TAXSAVING)