class Solution:
    def minimumSum(self, num):
        d = sorted(map(int, str(num)))
        return d[0] * 10 + d[1] * 10 + d[2] + d[3]