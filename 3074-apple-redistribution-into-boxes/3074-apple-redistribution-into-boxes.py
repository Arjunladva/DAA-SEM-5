class Solution:
    def minimumBoxes(self, apple, capacity):
        total = sum(apple)

        capacity.sort(reverse=True)

        count = 0

        for c in capacity:
            total -= c
            count += 1

            if total <= 0:
                return count

        return count