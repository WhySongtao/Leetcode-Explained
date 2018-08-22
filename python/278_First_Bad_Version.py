# Idea is basically binary search.
# I have always confused with the while loop condition. When is it "<" and when is it
# "<=". In my understanding, this depends on whether the last element (when start == end)
# has been checked or not. In this case, end is pointing to mid element which we have
# already checked, so we use "<".
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while (start < end):
            mid = start + (end - start) // 2
            if not isBadVersion(mid):
                start = mid + 1
            else:
                end = mid

        # At the end, start and point will point to the same element.
        return end
