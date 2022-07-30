"""
Problem name:   Longest Common Subsequence
Problem rank:   Medium
Problem URL:    https://leetcode.com/problems/longest-common-subsequence/
Runtime:        387 ms  (Faster than 95.42% of other submissions)
Memory Usage:   22.7 MB (58.24% better than other submissions)
Submission URL: https://leetcode.com/submissions/detail/760487544/
"""


class Solution:
    # Time and space complexity is O (n * m)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)]
              for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            print(f"Value of i is: {i}")
            for j in range(len(text2) - 1, -1, -1):
                print(f"Value of j is: {j}")
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # O (n * m)
        return dp[0][0]


sol = Solution()

text1 = "cbda"
text2 = "acadb"
print(
    f"The LCS of the previous strings is {sol.longestCommonSubsequence(text1, text2)}")
