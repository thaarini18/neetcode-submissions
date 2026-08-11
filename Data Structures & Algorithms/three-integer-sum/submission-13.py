class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i, a in enumerate(nums):

            if a > 0:
                break

            if i > 0 and a == nums[i-1]:
                continue

            target = -a
            low = i + 1
            high = len(nums) - 1

            while low < high:
                csum = nums[low] + nums[high]

                if csum > target:
                    high -= 1

                elif csum < target:
                    low += 1

                else:
                    output.append([a, nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while(low<high and nums[low]==nums[low-1]):
                        low+=1

        return output