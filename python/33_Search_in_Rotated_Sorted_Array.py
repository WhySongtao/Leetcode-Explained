# Thought: What makes this question different from a normal binary search is that
# in this question, there is an increase followed by an decrease. Depending on
# whether the middle point is in the increasing part or the decreasing part, we
# will shrink the size differently. So the first solution is simply state all
# the possible situation and shrink low and high range accordingly.

def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        answer = -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            middle = (low + high) // 2
            if target == nums[middle]:
                return middle

            # middle point is in the increasing(left) side
            if nums[middle] >= nums[low]:
                # target
                if nums[low] <= target <= nums[middle]:
                    high = middle - 1
                else:
                    low = middle + 1
            else:
                if nums[high]>=target>=nums[middle]:
                    low = middle + 1
                else:
                    high = middle - 1
        return answer
