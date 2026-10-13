class Solution:
    def diStringMatch(self, s: str):
        lo, hi = 0, len(s)
        ans = []
        for c in s:
            if c == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1
        ans.append(lo)
        return ans