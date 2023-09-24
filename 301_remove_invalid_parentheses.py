from typing import List


class Solution:
    isMoreOpenPar = False
    isMoreClosePar = False
    symbol = None
    index = None
    answer = []

    def checkInvalidParentheses(self, s: str):

        result = 0
        for i, par in enumerate(s):
            if par == "(":
                result += 1
            elif par == ")":
                if result == 0:
                    self.symbol = s
                    self.index = i
                    self.isMoreClosePar = True
                    break
                result -= 1
        else:
            if result == 0:
                print('ok')
                return [s]
            else:
                self.isMoreOpenPar = True

    def removeInvalidParentheses(self, s: str) -> List[str]:
        while True:
            self.checkInvalidParentheses(s)
            if not self.isMoreClosePar and not self.isMoreOpenPar:
                self.answer.append(s)
                return self.answer
            if self.isMoreClosePar:
                stringlist = list(s)
                del stringlist[self.index]
                s = "".join(stringlist)
                self.index = None
                self.isMoreClosePar = False


a = Solution()
print(a.removeInvalidParentheses('()())()'))
a.answer = []
print(a.removeInvalidParentheses('()()()'))
a.answer = []
print(a.removeInvalidParentheses('(())()'))
# a.removeInvalidParentheses(')(')
# a.removeInvalidParentheses('(')
# a.removeInvalidParentheses(')')
# a.removeInvalidParentheses('')
