class Solution:
    def minTimeToType(self, word: str) -> int:
        cur = 'a'
        ans = 0
        for c in word:
            d = abs(ord(c) - ord(cur))
            ans += min(d, 26 - d) + 1
            cur = c
        return ans