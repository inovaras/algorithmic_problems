from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for elem in nums:
            if elem in d:
                d[elem] += 1
            else:
                d[elem] = 1
        max_k = - 10 ^ 9
        max_v = 0
        for key, val in d.items():
            if val > max_v:
                max_k = key
                max_v = val
        return max_k


a = Solution()
print(a.majorityElement([1, 2, 1]))
print(a.majorityElement([2,2,1,1,1,2,2]))
print(a.majorityElement([3,2,3]))
print(a.majorityElement([1, 2, 1]))
