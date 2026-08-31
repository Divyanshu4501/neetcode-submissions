class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        counter = 0
        
        while j>=0 and nums[j] == val:
            counter += 1
            j -= 1
        
        while i<=j:
            if nums[i] != val:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                counter += 1
        
        return len(nums) - counter