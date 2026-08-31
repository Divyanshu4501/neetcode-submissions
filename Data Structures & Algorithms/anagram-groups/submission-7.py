class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))

            if key not in hmap:
                hmap[key] = [strs[i]]
            
            else:
                hmap[key].append(strs[i])

        return list(hmap.values())
