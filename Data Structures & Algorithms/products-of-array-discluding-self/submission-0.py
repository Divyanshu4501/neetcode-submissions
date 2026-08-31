class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []

        for i in range(len(nums)):
            p_element = 1
            for j in range(0, i):
                p_element *= nums[j]
            prefix.append(p_element)

            s_element = 1
            for k in range(i+1, len(nums)):
                s_element *= nums[k]
            suffix.append(s_element)

        return [i*j for i,j in zip(prefix,suffix)
        ]