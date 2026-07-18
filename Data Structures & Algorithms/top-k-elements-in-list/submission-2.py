class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for ele in nums:
          counts[ele] = 1 + counts.get(ele,0)

        freq = [[] for i in range (len(nums)+1)]
        for v,c in counts.items():
          freq[c].append(v)
       
        res = []
        for i in range (len(freq)-1, 0, -1):
          for val in freq[i]:
               res.append(val)
               if len(res) >= k:
                    return res
