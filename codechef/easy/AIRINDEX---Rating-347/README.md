# AIRINDEX - Rating 347

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Air Quality Index

In the light of `G-20` summit, government has decided to keep the average air quality index (AQI)  **strictly below**  $100$.
On some random day, Chef measures the AQI and found the value to be $X$.

Find whether the government was able to keep the AQI within limits.

### Input Format
- The input consists of an integer $X$ — the AQI Chef measured.
### Output Format

Output `YES`, if the government was able to keep the AQI within limits and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

### Constraints
- $1 \leq X \leq 150$
### Sample 1:
Input
Output

```
50

```

```
YES

```

### Explanation:

The AQI is strictly less than $100$. Thus, the government was able to keep the AQI within limits.

### Sample 2:
Input
Output

```
100

```

```
NO

```

### Explanation:

The AQI is equal to $100$. Thus, the government was not able to keep the AQI within limits.

### Sample 3:
Input
Output

```
99

```

```
YES
```

### Explanation:

The AQI is strictly less than $100$. Thus, the government was able to keep the AQI within limits.

### Sample 4:
Input
Output

```
145

```

```
NO
```

### Explanation:

The AQI is greater than $100$. Thus, the government was not able to keep the AQI within limits.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T13:19:49.364Z  

```py
# cook your dish here
x = int(input())
if(x<100):
    print("yes")
else:
    print("no")
    
```

---

[View on CodeChef](https://www.codechef.com/problems/AIRINDEX)