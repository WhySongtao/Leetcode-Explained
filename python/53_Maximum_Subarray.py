class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        # We need this line! Why? Because we can't set global_maximum to zero Because
        # we may have an all negative array as input.
        global_maximum = curr_maximum = nums[0]

        for i in range(1, len(nums)):
            # Essentially, we are testing if the previous element makes my maximum
            # even smaller. If so, we don't need it. We start from scratch.
            curr_maximum = max(nums[i], nums[i] + curr_maximum)
            global_maximum = max(global_maximum, curr_maximum)

        return global_maximum
