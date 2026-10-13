class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = ans = 0
        for c in s:
            balance += 1 if c == 'L' else -1
            if balance == 0:
                ans += 1
        return ans