class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        best = ""
        for i, c in enumerate(number):
            if c == digit:
                candidate = number[:i] + number[i + 1:]
                if candidate > best:
                    best = candidate
        return best