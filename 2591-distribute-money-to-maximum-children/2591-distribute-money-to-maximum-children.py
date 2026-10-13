class Solution:
    def distMoney(self, money, children):
        if money < children:
            return -1

        money -= children
        full = min(money // 7, children)
        money -= full * 7
        children -= full

        if children == 0:
            return full if money == 0 else full - 1
        if children == 1 and money == 3:
            return full - 1
        return full