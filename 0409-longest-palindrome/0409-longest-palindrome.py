class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        ans = sum((v // 2) * 2 for v in freq.values())
        return ans + (1 if any(v % 2 for v in freq.values()) else 0)