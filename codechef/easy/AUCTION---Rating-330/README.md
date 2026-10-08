# AUCTION - Rating 330

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Bidding

Alice, Bob and Charlie are bidding for an artifact at an auction.
Alice bids $A$ rupees, Bob bids $B$ rupees, and Charlie bids $C$ rupees (where $A$, $B$, and $C$ are  **distinct**).

According to the rules of the auction, the person who bids the  **highest**  amount will win the auction.
Determine who will win the auction.

### Input Format
- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains three integers $A$, $B$, and $C$, — the amount bid by Alice, Bob, and Charlie respectively.
### Output Format

For each test case, output who (out of `Alice`, `Bob`, and `Charlie`) will win the auction.

You may print each character of `Alice`, `Bob`, and `Charlie` in uppercase or lowercase (for example, `ALICE`, `aliCe`, `aLIcE` will be considered identical).

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq A, B, C \leq 1000$
- $A$, $B$, and $C$ are distinct.
### Sample 1:
Input
Output

```
4
200 100 400
155 1000 566
736 234 470
124 67 2

```

```
Charlie
Bob
Alice
Alice

```

### Explanation:

 **Test Case $1$:**  Charlie wins the auction since he bid the highest amount.

 **Test Case $2$:**  Bob wins the auction since he bid the highest amount.

 **Test Case $3$:**  Alice wins the auction since she bid the highest amount.

 **Test Case $4$:**  Alice wins the auction since she bid the highest amount.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-08T14:01:23.553Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    a, b, c = map(int,input().split())
    if(a>b and a>c):
        print("alice")
    elif(b>a and b>c):
        print("bob")
    else:
        print("charlie")
```

---

[View on CodeChef](https://www.codechef.com/problems/AUCTION)