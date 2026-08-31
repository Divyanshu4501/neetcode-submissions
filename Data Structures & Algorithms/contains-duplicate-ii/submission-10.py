class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        def duplicateSubarray(i,j):
            s = set()
            for num in nums[i:i+j+1]:
                s.add(num)
            return len(s) != len(nums[i:i+j+1])

        if k >= len(nums):
            return duplicateSubarray(0,len(nums)-1)
        for i in range(len(nums)-k):
            if duplicateSubarray(i,k):
                return True
        
        return False