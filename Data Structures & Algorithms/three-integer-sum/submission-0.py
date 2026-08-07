class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output=[]

        for i in range(len(nums)):
            low = i + 1
            high = len(nums) - 1

            while low < high:
                s = nums[i] + nums[low] + nums[high]

                if s == 0 and [nums[i],nums[low],nums[high]] not in output:
                    output.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                elif s < 0:
                    low += 1
                else:
                    high -= 1
        return output