class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output =[]
        for i in range (1,len(nums)):
            for j in range (i,0,-1):
                if ( nums[j-1] + nums[i] ) == target:
                    output.append(j-1)
                    output.append(i)
                    break
        return output