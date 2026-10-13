class Solution:
    def convertTime(self, current, correct):
        a = int(current[:2]) * 60 + int(current[3:])
        b = int(correct[:2]) * 60 + int(correct[3:])
        diff = b - a
        ans = 0
        for step in (60, 15, 5, 1):
            ans += diff // step
            diff %= step
        return ans