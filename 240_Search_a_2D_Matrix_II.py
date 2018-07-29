'''
Thought: When I saw something like sorted, I will always check if binary search
can be used to shrink the range. Here is the same.
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Take this as an example. First let's go to the middle of the first row: 7. If
the target is bigger, then clearly, it could be at the right of 7. It can also be
at the down of 7. The only impossible place is the element on the left of 7 in the
same row. Hmm, this doesn't look like a way to shrink range.

So what about going from right top corner. Corner seems to be a good starting point.
If the target is bigger than current element, we can get rid of this whole row!
If the target is smaller than the current element, we can get rid of this whole
column!

I think going from left bottom corner works as well.
'''
def searchMatrix(matrix, target):

    if len(matrix) == 0:
            return False
        # Starting from top right corner.
        row = 0
        column = len(matrix[0])-1

        while(row <= len(matrix)-1 and (column >= 0)):
            if matrix[row][column] == target:
                return True
            elif target < matrix[row][column]:
                column -= 1
            elif target > matrix[row][column]:
                row += 1

        return False
