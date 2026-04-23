# 📘 Minimum Sum Partition (Dynamic Programming)

## 🔗 Problem Source
GeeksforGeeks

---

## 🧾 Problem Statement

Given an array `arr[]` containing non-negative integers, divide it into two subsets such that:

> The absolute difference between the sums of the two subsets is minimum.

---

## 🧠 Intuition

Let:
- Total sum = `S`
- Subset sums = `S1` and `S2`

We know:

S1 + S2 = S


So, difference:

|S1 - S2| = |S - 2*S1|


👉 Therefore, the problem reduces to:

> Find a subset with sum as close as possible to `S/2`

---

## ⚙️ Algorithm

### Step 1: Compute Total Sum

S = sum(arr)


### Step 2: Define Target

target = S // 2


### Step 3: Initialize DP Array

- Create a boolean array `dp` of size `target + 1`
- `dp[j] = True` means subset sum `j` is possible


dp[0] = True


---

### Step 4: Fill DP Array

For each element `num` in array:


for num in arr:
for j in range(target, num - 1, -1):
dp[j] = dp[j] or dp[j - num]


👉 Reverse iteration ensures **each element is used only once (0/1 Knapsack)**

---

### Step 5: Find Best Possible Sum


for j in range(target, -1, -1):
if dp[j] == True:
subset_sum = j
break


---

### Step 6: Compute Final Answer


answer = S - 2 * subset_sum


---

## 💻 Python Implementation

```python
class Solution:
    def minDifference(self, arr, n):
        total_sum = sum(arr)
        target = total_sum // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        for j in range(target, -1, -1):
            if dp[j]:
                return total_sum - 2 * j
```
---

## 🧪 Example
**Input:**
`arr = [3, 1, 4, 2, 2]`

**Step:**
Total sum = 12
Target = 6

DP finds subset sum = 6

**Output:**
Minimum Difference = 0

---

## 🧩 Explanation
One possible partition:
* Subset1 = `[3, 1, 2]` → sum = 6
* Subset2 = `[4, 2]`   → sum = 6

Difference:
`|6 - 6| = 0`
---
## ⏱️ Complexity Analysis
**Time Complexity:**
`O(N × S)`

**Space Complexity:**
`O(S)`

*Where:*
* `N` = number of elements
* `S` = total sum / 2
---
## 🔑 Key Concepts Used
* Dynamic Programming
* Subset Sum Problem
* 0/1 Knapsack Pattern
---
## 🎯Important Points
* We only consider sums up to S/2
* DP array stores possibility, not actual subsets
* Reverse iteration prevents reuse of elements
---
## 🎓 Conclusion
The Minimum Sum Partition problem is a classic example of reducing a partition problem into a subset sum problem using dynamic programming. It demonstrates optimization techniques and is widely used in coding interviews.
---