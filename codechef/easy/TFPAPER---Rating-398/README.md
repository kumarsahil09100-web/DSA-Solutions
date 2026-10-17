# TFPAPER - Rating 398

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### True and False Paper

Alice wrote an exam containing $N$ true or false questions (i.e. questions whose answer is either true or false). Each question is worth $1$ mark and there is no negative marking in the examination. Alice scored $K$ marks out of $N$.

Bob wrote the same exam but he marked each and every question as the opposite of what Alice did, i.e, for whichever questions Alice marked `true`, Bob marked `false` and for whichever questions Alice marked `false`, Bob marked `true`.

Determine the score of Bob.

### Input Format
- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space-separated integers $N$ and $K$ — the total number of questions in the exam and the score of Alice.
### Output Format

For each test case, output on a new line the score of Bob.

### Constraints
- $1 \leq T \leq 2000$
- $1 \le N \le 100$
- $0 \le K \le N$
### Sample 1:
Input
Output

```
3
1 1
50 0
100 76

```

```
0
50
24

```

### Explanation:

 **Test case $1$:**  There was one question in the exam and Alice answered it correctly. This means that Bob will surely answer it incorrectly. Therefore Bob's score is zero.

 **Test case $2$:**  Alice answered all the questions incorrectly, and so Bob will surely answer all the questions correctly. Therefore Bob's score is $50$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T14:03:37.174Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    print(n-k)

```

---

[View on CodeChef](https://www.codechef.com/problems/TFPAPER)