class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        r = (len(nums) - k)
        nums[:r] = nums[:r][::-1]
        nums[r:] = nums[r:][::-1]
        nums[:] = nums[::-1]