class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # keep differrence/rest as hash/dict key
        temp_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] not in temp_dict:
                temp_dict[diff] = i
            else:
                return [temp_dict[nums[i]], i]

def main():
    test = Solution()
    assert test.twoSum([2,7,11,15], 9) == [0, 1]
    assert test.twoSum([3, 2, 4], 6) == [1, 2]
    assert test.twoSum([3, 3], 6) == [0, 1]

if __name__ == '__main__':
    main()