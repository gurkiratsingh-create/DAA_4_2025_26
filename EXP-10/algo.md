# 🧩 LeetCode 115: Distinct Subsequences

## 📌 Problem Statement

Given two strings `s` (source) and `t` (target), return the number of distinct subsequences of `s` which equals `t`.

A subsequence is formed by deleting some (or no) characters from `s` without changing the order of the remaining characters.

---

## 🧠 Intuition

At every character of `s`, we have two choices:

- Take it (if it matches the current character of `t`)
- Skip it

This makes it a **counting problem**, similar to:
- Subsequence counting
- Subset counting
- Knapsack (count ways)

---

## 🔧 Dynamic Programming Approach

### 📊 State Definition

dp[i][j] = number of ways to form t[0...j-1] using s[0...i-1]

---

### 🎯 Base Cases

- dp[i][0] = 1 → Empty string `t` can always be formed  
- dp[0][j] = 0 → Non-empty `t` cannot be formed from empty `s`

---

### 🔁 Transition

If characters match:

dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

If characters do not match:

dp[i][j] = dp[i-1][j]

---

## 🧮 Algorithm (Step-by-Step)

1. Let m = length of s, n = length of t  
2. Create a 2D DP array of size (m + 1) × (n + 1)  
3. Initialize:
   - dp[i][0] = 1 for all i  
   - dp[0][j] = 0 for all j > 0  
4. Loop through i from 1 to m:
   - Loop through j from 1 to n:
     - If s[i-1] == t[j-1]:
       - dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
     - Else:
       - dp[i][j] = dp[i-1][j]
5. Return dp[m][n]

---

## 💻 Code Implementation (Python)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]

---

## ⚡ Space Optimization (1D DP)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(t)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, len(s) + 1):
            for j in range(n, 0, -1):  # reverse traversal
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]

---

## ⏱️ Complexity Analysis

### 🟢 Time Complexity

O(m × n)

We fill a DP table of size (m + 1) × (n + 1)

---

### 🟡 Space Complexity

2D DP:

O(m × n)

Optimized 1D DP:

O(n)

---

## ✅ Example

Input:

s = "babgbag"  
t = "bag"

Output:

5

---

## 🧠 Key Takeaway

This is a "take / not take" DP pattern:

If match:
    take + not take

If not match:
    skip only

This pattern appears in:

- Subsequence counting  
- Subset sum counting  
- Knapsack variations  

---

## 🚀 Final Thoughts

- Always think in terms of choices  
- Convert recursion → memoization → tabulation  
- Focus on patterns, not just individual problems  

Master this → many DP problems become easy.