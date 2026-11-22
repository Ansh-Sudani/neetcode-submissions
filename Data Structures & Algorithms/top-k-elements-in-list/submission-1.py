class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        hlist = []
        for i in range (len(nums)):
            if nums[i] in hmap:
                hmap[nums[i]] += 1
            else:
                hmap[nums[i]] = 1
        smap = sorted(hmap.items(), key=lambda x:x[1], reverse = True)
        for key,val in smap[:k]:
            hlist.append(key)
        return hlist