class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myList = []
        mydict = {}
        for num in nums:
            if num in mydict:
                mydict[num] += 1
            else:
                mydict[num] = 1
        sorted_items = sorted(mydict.items(), key=lambda x: x[1], reverse=True)
        for num, count in sorted_items[:k]:
            myList.append(num)
        return myList   
        