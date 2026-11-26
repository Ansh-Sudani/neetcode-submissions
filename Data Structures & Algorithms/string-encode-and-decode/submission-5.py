class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for wrd in strs:
            ln = str(len(wrd))
            s += ln + '#' + wrd
        return s

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        while i < len(s):
            hi = s.find('#',i)
            dg = int(s[i:hi])
            lst.append(s[hi+1:hi+1+dg])
            i = hi + 1 + dg
        return lst