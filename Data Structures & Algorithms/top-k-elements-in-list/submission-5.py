class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        lst = []
        for i in range(len(nums)):
            if nums[i] in hmap:
                hmap[nums[i]] += 1
            else:
                hmap[nums[i]] = 1
        srted = sorted(hmap.items(), key = lambda x:x[1], reverse=True)
        for key,val in srted[:k]:
            lst.append(key)
        return lst