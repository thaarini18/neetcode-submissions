class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for ch in strs:
          ss = ''.join(sorted(ch))
          output[ss].append(ch)
        return list(output.values())