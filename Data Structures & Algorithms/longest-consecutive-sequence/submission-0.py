class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h_set = set(nums)
        sos = []

        for i in range(len(nums)):
            if nums[i] - 1 not in h_set:
                sos.append(nums[i])
        count  = 0
        for i in range(len(sos)):
            temp_count = 0
            temp = sos[i]
            while True:
                if temp in h_set:
                    temp_count += 1
                    temp += 1

                else:
                    break

            if temp_count>count:
                count = temp_count

        return count
    
        