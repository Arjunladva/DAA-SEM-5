class Solution:
    def minDeletion(self, s, k):
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        if len(freq) <= k:
            return 0

        frequencies = sorted(freq.values())

        delete_count = len(freq) - k

        return sum(frequencies[:delete_count])