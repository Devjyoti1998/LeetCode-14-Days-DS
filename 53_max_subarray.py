class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        actual_max=nums[0]
        curr_max=nums[0]

        for num in nums[1:]:
            curr_max=max(num,curr_max+num)
            actual_max=max(actual_max,curr_max)
        return actual_max

        
