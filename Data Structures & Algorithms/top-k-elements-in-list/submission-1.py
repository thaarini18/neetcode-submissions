class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for ele in nums:
          counts[ele] = 1 + counts.get(ele,0)
        freq = [[] for i in range (len(nums)+1)]
        for v,f in counts.items():
          freq[f].append(v)
        res = []
        for i in range (len(freq)-1, 0, -1):
          for j in freq[i]:
               res.append(j)
               if len(res)>=k:
                    return res
