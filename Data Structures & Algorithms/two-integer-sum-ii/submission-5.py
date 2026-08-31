class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while True and left<right:
            if numbers[left] + numbers[right] < target:
                left += 1
            
            elif numbers[left] + numbers[right] > target:
                right -= 1

            else:
                if left != right:
                    return [left+1, right+1]

        return []