class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h_set = set(nums)
        count = 0
        
        for num in h_set:
            if num-1 not in h_set:
                temp = num
                temp_count = 0
                while temp in h_set:
                    temp += 1
                    temp_count += 1
                count = max(count, temp_count)

        return count