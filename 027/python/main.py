from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ## solution 1: fail, but pass in local
        ## the nums is different with online judgement        
        #return len([ n for n in nums if n != val ])
    
        # solution 2
        while val in nums:
            nums.remove(val)
        return len(nums)

def main():
    test = Solution()
    assert test.removeElement([3, 2, 2, 3], 3) == 2
    assert test.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5

if __name__ == '__main__':
    main()