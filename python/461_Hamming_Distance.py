'''
First key point: XOR.
Second key point: z &= (z-1) will knock out the lowest one. 
'''

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        count = 0
        while (z):
            count += 1;
            z &= (z-1)

        return count
