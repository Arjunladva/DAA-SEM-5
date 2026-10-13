class Solution:
    def maximum69Number(self, num):
        a = list(str(num))
        for i, c in enumerate(a):
            if c == '6':
                a[i] = '9'
                break
        return int(''.join(a))