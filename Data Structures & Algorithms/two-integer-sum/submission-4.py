class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []

        pairs = [(num, idx) for idx,num in enumerate(nums)]
        pairs.sort(key= lambda x: x[0])

        i = 0
        j = len(nums) - 1

        while i<j:
            if pairs[i][0] + pairs[j][0] == target:
                return sorted([pairs[i][1], pairs[j][1]])
                
            elif pairs[i][0] + pairs[j][0] < target:
                i += 1

            else:
                j -= 1
