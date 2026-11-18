class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict1 = {}
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key in mydict1:
                mydict1[key].append(strs[i])
            else:
                mydict1[key] = [strs[i]]
        return list(mydict1.values())
        