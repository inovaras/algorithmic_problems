from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_list_i = 0
        finish_list_i = len(matrix)
        while start_list_i < finish_list_i:
            medium_list_i = start_list_i + (finish_list_i - start_list_i) // 2
            start_elem_i = 0
            finish_elem_i = len(matrix[medium_list_i])
            flag = ''
            while start_elem_i < finish_elem_i - 1:
                medium_elem_i = start_elem_i + (finish_elem_i - start_elem_i) // 2
                if target == matrix[medium_list_i][medium_elem_i]:
                    return True
                elif target > matrix[medium_list_i][medium_elem_i]:
                    start_elem_i = medium_elem_i
                    flag = 'right_part'
                elif target < matrix[medium_list_i][medium_elem_i]:
                    finish_elem_i = medium_elem_i
                    flag = 'left_part'
            else:
                if matrix[medium_list_i][start_elem_i] == target:
                    flag = 'true'
            if flag == 'right_part':
                start_list_i = medium_list_i + 1
            elif flag == 'left_part':
                finish_list_i = medium_list_i
            elif flag == '':
                if matrix[medium_list_i][0] == target and len(matrix) == 1:
                    return True
                elif matrix[medium_list_i][0] > target:
                    finish_list_i = medium_list_i
                elif matrix[medium_list_i][0] < target:
                    start_list_i = medium_list_i + 1
            elif flag == 'true':
                return True
        else:
            return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
a = Solution()
print(1, a.searchMatrix(matrix, target) == True)

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
a = Solution()
print(2, a.searchMatrix(matrix, target) == False)

matrix = [[1, 13, 8]]
target = 13
a = Solution()
print(3, a.searchMatrix(matrix, target) == True)

matrix = [[1, 3, 5]]
target = 1
a = Solution()
print(4, a.searchMatrix(matrix, target) == True)


matrix = [[1]]
target = 1
a = Solution()
print(5, a.searchMatrix(matrix, target) == True)


matrix = [[1]]
target = 13
a = Solution()
print(6, a.searchMatrix(matrix, target) == False)

matrix = [[1], [3]]
target = 1
a = Solution()
print(7, a.searchMatrix(matrix, target) == True)

matrix = [[1], [3], [4]]
target = 4
a = Solution()
print(8, a.searchMatrix(matrix, target) == True)