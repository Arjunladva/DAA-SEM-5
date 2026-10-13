class Solution:
    def getLongestSubsequence(self, words, groups):
        ans = []

        for i in range(len(words)):
            if i == 0 or groups[i] != groups[i - 1]:
                ans.append(words[i])

        return ans