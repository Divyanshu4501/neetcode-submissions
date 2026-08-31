class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        arr = sorted(nums)
        return arr[len(arr)//2]