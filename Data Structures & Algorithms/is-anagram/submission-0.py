class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mydict1 = {}
        mydict2 = {}
        for char in s:
            if char in mydict1:
                mydict1[char] += 1
            else:
                mydict1[char] = 1
        for char in t:
            if char in mydict2:
                mydict2[char] += 1
            else:
                mydict2[char] = 1
        return mydict1 == mydict2