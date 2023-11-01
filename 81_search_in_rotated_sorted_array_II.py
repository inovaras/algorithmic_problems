from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            return nums[0] == target
        first_i = 0
        last_i = len(nums) - 1
        while first_i < last_i:
            mid_i = first_i + (last_i - first_i) // 2
            mid = nums[mid_i]
            first = nums[first_i]
            last = nums[last_i]
            if last_i - first_i == 1:
                return nums[last_i] == target or nums[first_i] == target
            if mid == target:
                return True
            elif first < mid < last:
                if mid > target:
                    last_i = mid_i - 1
                elif mid < target:
                    first_i = mid_i + 1
                else:
                    return mid_i
            elif first == mid != last:
                first_i = mid_i
            elif first != mid == last:
                last_i = mid_i
            elif first == mid == last:
                tmp = mid_i
                dif = last_i - first_i
                # здесь надо написать метод двоичного поиска для неубывающего списка
                while first_i < mid_i:
                    if nums[mid_i-1] == nums[mid_i]:
                        mid_i = mid_i - 1
                    else:
                        if nums[mid_i] == target:
                            return True
                        last_i = mid_i
                        break

                while tmp < last_i:
                    if nums[tmp-1] == nums[tmp]:
                        tmp = tmp + 1
                    else:
                        if nums[tmp] == target:
                            return True
                        first_i = tmp
                        break
                if last_i - first_i == dif:
                    return False
            elif first > mid < last:
                # нарушена первая половина списка
                if mid == target:
                    return True
                elif mid < target <= last:
                    first_i = mid_i + 1
                # elif target == last:
                #     return True
                else:
                    last_i = mid_i - 1

            elif first < mid > last:
                # нарушена вторая половина списка
                if mid == target:
                    return True
                elif first <= target < mid:
                    last_i = mid_i - 1
                # elif first == target:
                #     return True
                else:
                    first_i = mid_i + 1
        else:
            return nums[first_i] == target


a = Solution()
print(a.search(nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], target=2) is True)
print(a.search(nums=[1, 1], target=0) is False)
print(a.search(nums=[1, 0, 1, 1, 1], target=0) is True)
print(a.search(nums=[1, 2, 1], target=2) is True)
print(a.search(nums=[1, 1, 1], target=2) is False)
print(a.search(nums=[1, 3, 5], target=1) is True)
print(a.search(nums=[2, 5, 6, 0, 0, 1, 2], target=3) is False)
print(a.search(nums=[2], target=2) is True)
print(a.search(nums=[2], target=0) is False)
