from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(a):
            n = len(a)
            if n <= 1:
                return a

            mid = n // 2
            left = merge_sort(a[:mid])
            right = merge_sort(a[mid:])

            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            while i < len(left):
                merged.append(left[i])
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        return merge_sort(nums)
