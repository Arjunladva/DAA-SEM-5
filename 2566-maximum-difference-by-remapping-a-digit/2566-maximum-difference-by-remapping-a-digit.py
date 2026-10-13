class Solution:
    def minMaxDifference(self, num):
        s = str(num)
        repl = next((c for c in s if c != '9'), None)
        maximum = s if repl is None else s.replace(repl, '9')
        minimum = s.replace(s[0], '0')
        return int(maximum) - int(minimum)