class Solution:
    def merge(self, left : List[int], right : List[int]) -> List[int]:
        ans = []
        i = 0
        j = 0
        while i<len(left) and j<len(right):
            if left[i] >= right[j]:
                ans.append(right[j])
                j += 1
            
            else:
                ans.append(left[i])
                i += 1

        while i < len(left):
            ans.append(left[i])
            i += 1

        while j < len(right):
            ans.append(right[j])
            j += 1

        return ans

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left  = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)
        
        