class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        _sum = nums[0]
        _len = float('inf')

        i, j = 0, 1
        while j <= len(nums):
            if _sum < target:
                if j<len(nums):
                    _sum += nums[j]
                    j += 1
                else:
                    break
            else:
                _len = min(_len, j-i)
                _sum -= nums[i]
                i += 1
        return _len