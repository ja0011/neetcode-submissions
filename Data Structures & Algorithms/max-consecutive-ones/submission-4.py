class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a, b = len(nums), 0

        for i in range(a):
            ct = 0
            for j in range(i,a):
                if nums[j] == 0: break
                ct += 1
            b = max(b ,ct)
        return b
        