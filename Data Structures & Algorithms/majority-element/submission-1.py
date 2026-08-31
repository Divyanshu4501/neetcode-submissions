class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 1
        win = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == win:
                counter += 1
            else:
                if counter > 0:
                    counter -= 1
                else:
                    win = nums[i]

        return win