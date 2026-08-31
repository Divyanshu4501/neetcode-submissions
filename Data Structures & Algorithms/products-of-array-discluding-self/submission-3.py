class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #suffix
        suffix = [1]*n
        prefix = [1]*n
        j = n-2
        for i in range(1,n):
            suffix[i] = nums[i-1]*suffix[i-1]
            if j >= 0:
                prefix[j] = nums[j+1]*prefix[j+1]
                j -= 1

        return [x*y for x,y in zip(suffix,prefix)]
                