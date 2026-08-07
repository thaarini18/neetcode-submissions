class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i,num in enumerate(nums):
            target = -num
            if num > 0:
                break # no negative nums exist, can't sum to 0
            # how do we prevent duplicates?
            # => this will happen if iterated num (idx i) is the same as previous
            if i > 0 and num == nums[i-1]:
                continue # skip to next idx i

            # now, we use two pointers
            j = i+1 # left
            k = len(nums)-1 # right
            while j < k:
                if (nums[j] + nums[k] > target):
                    k -= 1
                elif (nums[j] + nums[k] < target):
                    j += 1
                else:
                    res.append([num, nums[j], nums[k]])
                    k -= 1
                    j += 1

                    # adjust for duplicates on left
                    while (j < k and nums[j] == nums[j-1]):
                        j += 1
        return res
                
            



