class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []
        def find_closest(arr, x):
            low, high = 0, len(arr)-1
            idx = 0
            diff = float("inf")
            while low<=high:
                mid = (high- low)//2 + low
                if abs(x - arr[mid]) < diff:
                    diff = abs(x - arr[mid])
                    idx = mid
                if arr[mid] < x:
                    low = mid + 1
                elif arr[mid] > x:
                    high = mid - 1
                    
                else:
                    high = mid -1
            return idx
        
        idx = find_closest(arr, x)
        ans.append(arr[idx])
        count = 0
        i, j = idx - 1, idx + 1
        for _ in range(k-1):
            if i < 0:
                ans.append(arr[j])
                j += 1
            elif j >= len(arr):
                ans.append(arr[i])
                i -= 1
            elif abs(x - arr[i]) <= abs(x - arr[j]):
                ans.append(arr[i])
                i -= 1
            else:
                ans.append(arr[j])
                j += 1

        return sorted(ans)
            
