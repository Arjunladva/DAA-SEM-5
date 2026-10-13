class Solution:
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        take = min(k, numOnes)
        ans = take
        k -= take

        take = min(k, numZeros)
        k -= take

        take = min(k, numNegOnes)
        ans -= take

        return ans