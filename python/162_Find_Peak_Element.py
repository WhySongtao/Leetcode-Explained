"""
Thought before start: So in the note, it says: "Your solution should be in logarithmic complexity."
OK, now this just makes me instantly think of binary search. Does it work? Let's
check.
Scenario 1: nums[middle-1]<nums[middle]<nums[middle+1]
            Great! This is one of the peak element.
Scenario 2: nums[middle]<nums[middle+1]
            So middle is not a peak. Where is the peak. Let's have a look at the
            right hand side. There will be 3 scenarios:
            1. Right hand side will keep increasing. [4, 5, 6, 7, 8]
               Then there is a peak at the last index.
            2. Right hand side will increase first then decrease. [4, 5, 6, 5, 4]
               6 is the peak here so peak exists.
            3. Decrease first then increase. [4, 3, 2, 3, 4, 5]
               First peak is the left most element because nums[middle] is already
               less than nums[middle+1] which is the left most element in the
               right hand side. Another peak will be the last index same as first
               scenario.
Scenario 3: nums[middle]<nums[middle-1]
            Same as scenario 2.
"""
def findPeakElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return
        # We didn't check if there are at least 2 element in nums because the
        # while loop below deals with that.
        low = 0
        high = len(nums) - 1
        # Stop when there is only 2 elements left. for example [*, *, 4, 5, *, *, ..., *]
        while low < high-1:
            middle = (low + high) // 2
            # Scenario 1
            if nums[middle-1] < nums[middle] and nums[middle] > nums[middle+1]:
                return middle
            # Scenario 2
            if nums[middle] < nums[middle+1]:
                low = middle + 1
            else:
                nums[middle] < nums[middle-1]
                high = middle - 1

        # When there are only 2 elements left and you know there is a peak inside,
        # then you just need to find the bigger one.
        return low if nums[low] >= nums[high] else high
