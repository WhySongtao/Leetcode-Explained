'''
Thought: Have an index max_reach to keep track of the maximum index we can
reach so far. When looping through the array, if current index exceeds max_reach,
we know current index is not reachable.
'''

def canJump(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        for i, num in enumerate(nums):
            # If current location is already beyond the max reachable.
            if i > max_reach:
                return False
            else:
                max_reach = max(max_reach, i + num)

        return True
