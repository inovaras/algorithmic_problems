from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        first_i = 0
        last_i = len(nums) - 1
        while first_i <= last_i:
            mid_i = first_i + (last_i - first_i) // 2
            mid = nums[mid_i]
            first = nums[first_i]
            last = nums[last_i]
            if first <= mid <= last:
                if mid > target:
                    last_i = mid_i - 1
                elif mid < target:
                    first_i = mid_i + 1
                else:
                    return mid_i
            elif first >= mid <= last:
                # нарушена первая половина списка
                if mid == target:
                    return mid_i
                elif mid < target <= last:
                    first_i = mid_i + 1
                else:
                    last_i = mid_i - 1

            elif first <= mid >= last:
                # нарушена вторая половина списка
                if mid == target:
                    return mid_i
                elif first <= target < mid:
                    last_i = mid_i - 1
                else:
                    first_i = mid_i + 1
        else:
            return -1


a = Solution()
print(a.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0) == 4)
print(a.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3) == -1)
print(a.search(nums=[0, 1, 2, 4, 5, 6, 7], target=1) == 1)
print(a.search(nums=[0, 1, 2, 4, 5, 6, 7], target=7) == 6)
print(a.search(nums=[0, 1, 2, 4, 5, 6, 7], target=0) == 0)
print(a.search(nums=[1], target=0) == -1)
