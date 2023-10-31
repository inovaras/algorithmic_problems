from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        first_i = 0
        last_i = len(nums) - 1
        while first_i <= last_i:
            mid_i = first_i + (last_i - first_i) // 2
            mid = nums[mid_i]
            first = nums[first_i]
            last = nums[last_i]
            if last_i - first_i == 1:
                return min(first, last)
            if first <= mid <= last:
                return first
            elif first >= mid and first >= last:
                # нарушена первая половина списка
                last_i = mid_i

            elif first >= last and first <= mid:
                # нарушена вторая половина списка
                    first_i = mid_i
        else:
            return -1


a = Solution()
print(a.findMin(nums=[3, 4, 5, 1, 2]), 1)
print(a.findMin(nums=[3, 4]), 3)
print(a.findMin(nums=[5, 1]), 1)
print(a.findMin(nums=[0]), 0)
print(a.findMin(nums=[11, 13, 15, 17]), 11)
