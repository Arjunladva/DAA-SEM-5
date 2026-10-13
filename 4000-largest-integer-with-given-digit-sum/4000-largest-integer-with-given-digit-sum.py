class Solution:
    def largestInteger(self, n, s):
        if n * 9 < s:
            return -1

        ans = 0

        for _ in range(n):
            digit = min(s, 9)

            ans = ans * 10 + digit

            s -= digit

        return ans