class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n
        
        # Pass 1: Calculate prefix products directly in the result array
        prefix_product = 1
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]
            
        # Pass 2: Calculate suffix products on the fly and multiply with the result
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]
            
        return result