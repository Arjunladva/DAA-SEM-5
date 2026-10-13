class Solution:
    def splitNum(self, num):
        d = sorted(str(num))
        a = b = 0
        for i, c in enumerate(d):
            if i % 2 == 0:
                a = a * 10 + int(c)
            else:
                b = b * 10 + int(c)
        return a + b