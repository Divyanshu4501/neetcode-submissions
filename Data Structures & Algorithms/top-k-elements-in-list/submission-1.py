class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i,num in enumerate(nums):
            freq[num] = freq.get(num,0)+1
        sorted_freq = sorted(freq.items(), key = lambda x: x[1], reverse = True)
        return [num for num, i in sorted_freq[:k]]
