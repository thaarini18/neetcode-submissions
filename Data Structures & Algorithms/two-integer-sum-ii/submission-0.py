class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left < right:
            csum = numbers[left] + numbers[right]
            if csum < target :
                left += 1
            elif csum > target:
                right -= 1
            else:
                return [left+1 , right+1]
                