# CARTRIP - Rating 374

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Car Trip

Chef rented a car for a day.

Usually, the cost of the car is Rs $10$ per km. However, since Chef has booked the car for the whole day, he needs to pay for  **at least**  $300$ kms even if the car runs less than $300$ kms.

If the car ran $X$ kms, determine the cost Chef needs to pay.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $X$ - denoting the number of kms Chef travelled.
### Output Format

For each test case, output the cost Chef needs to pay.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X \leq 1000$
### Sample 1:
Input
Output

```
5
800
3
299
301
300

```

```
8000
3000
3000
3010
3000

```

### Explanation:

 **Test case $1$:**  The car runs for $800$ kms. Thus, he needs to pay $800\cdot 10 = 8000$ rupees.

 **Test case $2$:**  The car runs for $3$ kms. However, since Chef booked the car for whole day, he needs to pay for at least $300$ kms. Thus, he needs to pay $300\cdot 10 = 3000$ rupees.

 **Test case $3$:**  The car runs for $299$ kms. However, since Chef booked the car for whole day, he needs to pay for at least $300$ kms. Thus, he needs to pay $300\cdot 10 = 3000$ rupees.

 **Test case $4$:**  The car runs for $301$ kms. Thus, he needs to pay $301\cdot 10 = 3010$ rupees.

 **Test case $5$:**  The car runs for $300$ kms. Thus, he needs to pay $300\cdot 10 = 3000$ rupees.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-15T13:00:25.785Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    x = int(input())
    if(x<300):
        print(3000)
    else:
        print(x*10)
```

---

[View on CodeChef](https://www.codechef.com/problems/CARTRIP)