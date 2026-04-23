class Solution:
    def minDifference(self, arr):
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