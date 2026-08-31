class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a,b = None, None
        count_a, count_b = 0, 0
        
        for num in nums:
            if num == a:
                count_a += 1
            elif num == b:
                count_b += 1
            elif count_a == 0:
                a, count_a = num, 1
            elif count_b == 0:
                b, count_b = num, 1
            else:
                count_a -= 1
                count_b -= 1
        
        return [x for x in (a,b) if nums.count(x) > n//3]
