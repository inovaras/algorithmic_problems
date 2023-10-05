from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = dict()
        for elem in nums:
            if elem in d:
                d[elem] += 1
            else:
                d[elem] = 1
        answer = []
        times = len(nums) / 3
        print('times', times)
        for key, val in d.items():
            if val > times:
                answer.append(key)
        return answer


a = Solution()
print(a.majorityElement([3, 2, 3]))
print(a.majorityElement([1]))
print(a.majorityElement([1, 2]))
print(a.majorityElement([]))