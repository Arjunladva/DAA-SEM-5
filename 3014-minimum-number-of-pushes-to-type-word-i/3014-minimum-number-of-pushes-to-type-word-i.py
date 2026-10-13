class Solution:
    def minimumPushes(self, word):
        n = len(word)

        ans = 0
        cost = 1

        for i in range(n):
            if i > 0 and i % 8 == 0:
                cost += 1

            ans += cost

        return ans