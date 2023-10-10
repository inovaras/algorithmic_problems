# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def param(func):
    your_guess = int(input('напечатай число: '))

    def wrapper(num):
        if num < your_guess:
            return 1
        elif num > your_guess:
            return -1
        else:
            return 0
    return wrapper

@param
def guess(num: int) -> int:
    return num


class Solution:
    def guessNumber(self, n: int) -> int:
        start = 0
        finish = n
        while start <= finish:
            num = start + (finish - start)//2
            answer = guess(num)
            if answer == -1:
                finish = num
            elif answer == 1:
                start = num + 1
            elif answer == 0:
                return num


a = Solution()
print(a.guessNumber(6))
