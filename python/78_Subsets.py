# At each element, recursivly adding element to the templist and thrn add to the answer.

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        self.backtrack(answer, [], nums, 0)
        
        return answer
    
    def backtrack(self, answer, templist, nums, start):
        answer.append(templist)
        # Loop over each element.
        for i in range(start, len(nums)):
            templist.append(nums[i])
            self.backtrack(answer, templist[:], nums, i+1)
            # Before moving to the next element, we need to remove all the temp node to start fresh.
            templist.pop()
            