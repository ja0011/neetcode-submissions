class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = res = 0

        for num in nums:
            count = count + 1 if num else 0
            res = max(res, count)
        return res
            