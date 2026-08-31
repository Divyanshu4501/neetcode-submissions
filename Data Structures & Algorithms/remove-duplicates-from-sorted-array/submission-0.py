class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while True:
            if i<len(nums) and j<len(nums):
                if nums[i] == nums[j]:
                    nums.pop(j)
                else:
                    i += 1
                    j += 1
            else:
                break
        
        return len(nums)