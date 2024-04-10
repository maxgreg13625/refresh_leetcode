from typing import List

class Solution:
    def binary_search(self, nums: List[int], target: int, start: int, end: int):
        medium = (start + end) // 2

        if nums[medium] == target:
            return medium
        elif nums[medium] < target and medium == start:
            return medium + 1
        elif nums[medium] > target and medium == start:
            return medium
        elif nums[medium] < target:
            return self.binary_search(nums, target, medium, end)
        else:
            return self.binary_search(nums, target, start, medium)

    def searchInsert(self, nums: List[int], target: int) -> int:
        # solution 1: recursive
        length = len(nums)
        return self.binary_search(nums, target, 0, length)

def main():
    test = Solution()
    assert test.searchInsert([1, 3, 5, 6], 5) == 2
    assert test.searchInsert([1, 3, 5, 6], 2) == 1
    assert test.searchInsert([1, 3, 5, 6], 7) == 4
    assert test.searchInsert([1, 3, 5, 6], 0) == 0

if __name__ == '__main__':
    main()