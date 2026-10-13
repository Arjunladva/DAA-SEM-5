class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        a = list(s)
        l, r = 0, len(a) - 1
        while l < r:
            c = min(a[l], a[r])
            a[l] = a[r] = c
            l += 1
            r -= 1
        return ''.join(a)