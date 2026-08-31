class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num,frequency in freq.items():
            if frequency > n//3:
                res.append(num)
        
        return res