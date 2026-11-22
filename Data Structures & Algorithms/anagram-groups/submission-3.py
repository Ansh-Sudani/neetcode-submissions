class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for i in range (len(strs)):
            key = ''.join(sorted(strs[i]))
            if key in hmap:
                hmap[key].append(strs[i])
            else:
                hmap[key] = [strs[i]]
        return list(hmap.values())