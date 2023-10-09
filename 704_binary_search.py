from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        finish = len(nums)
        while start < finish:
            middle = start + (finish - start) // 2
            if target > nums[middle]:
                start = middle + 1
            elif target < nums[middle]:
                finish = middle
            else:
                return middle
        else:
            return -1


a = Solution()
print(a.search([1, 2, 3, 4, 5, 6, 7, 8], 8))
print(a.search([8], 8))
print(a.search([1, 2, 3, 4, 5, 6, 7], 8))
print(a.search([-1, 0, 3, 5, 9, 12], 9))
print(a.search([-1, 0, 3, 5, 9, 12], 2))
