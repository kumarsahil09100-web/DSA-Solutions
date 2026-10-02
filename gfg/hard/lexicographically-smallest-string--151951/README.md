# Lexicographically Smallest Rotation

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a string  **s**, find the lexicographically smallest string after rotating the string left any number of times including 0.

 **Example:** 

```
Input: s = "abcd"
Output: "abcd"
Explanation: String after each rotation are "abcd", "bcda", "cdab", "dabc" and so on. Lexicographically smallest among them is "abcd".

```

```
Input: s = "baca"
Output: "abac"
Explanation: Strings after each rotation are "baca", "acab", "caba", "abac" and so on. Lexicographically smallest among them is "abac".
```

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-02T06:06:38.285Z  

```cpp
class Solution {
  public:
    string lexiString(string &s) {
        // code here
       int n = s.size();

              // Double the string
              string ss = s + s;

              int i = 0, j = 1, k = 0;

              while (i < n && j < n && k < n) {

                  if (ss[i + k] == ss[j + k]) {
                      k++;
                  }
                  else if (ss[i + k] > ss[j + k]) {
                      i = i + k + 1;

                      if (i <= j)
                          i = j + 1;

                      k = 0;
                  }
                  else {
                      j = j + k + 1;

                      if (j <= i)
                          j = i + 1;

                      k = 0;
                  }
              }

              int start = min(i, j);

              return ss.substr(start, n);
    }
};
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/lexicographically-smallest-string--151951/1)