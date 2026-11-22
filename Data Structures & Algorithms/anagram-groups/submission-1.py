class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        hlst = []
        for i in range (len(strs)):
            key = "".join(sorted(strs[i]))
            if key in hmap: 
                hmap[key].append(strs[i])
            else:
                hmap[key] = [strs[i]]
        for key,val in hmap.items():
            hlst.append(hmap[key])
        return hlst