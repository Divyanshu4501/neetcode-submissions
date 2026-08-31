class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        for i in range(len(nums)):
            p_element = 1
            if i > 0:
                p_element = prefix[i-1]*nums[i-1]
            prefix.append(p_element)

        for j in range(len(nums) -1, -1, -1):
            s_element = 1
            if j < len(nums) - 1:
                s_element = suffix[0]*nums[j+1]
            suffix.insert(0,s_element)


        return [i*j for i,j in zip(prefix,suffix)]