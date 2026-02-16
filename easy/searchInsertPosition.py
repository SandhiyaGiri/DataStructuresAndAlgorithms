class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # start, end = 0, len(nums) - 1
        # mid = end / 2

        # if 

        ans = 0

        for i in range(0, len(nums)):
            if target == nums[i]:
                ans = i
                return ans
            elif target > nums[i]:
                ans = i+1

        return ans
        