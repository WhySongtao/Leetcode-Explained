"""
be careful! Everything in this grid is a character, not an int.
"""
def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    count = 0
    if grid is None:
        return 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                helper(grid, i, j)

    return count

def helper(grid, i, j):
    grid[i][j] = 0
    # up
    if i - 1 >= 0 and grid[i-1][j] == '1':
        helper(grid, i-1, j)
    # down
    if i + 1 <= len(grid)-1 and grid[i+1][j] == '1':
        helper(grid, i+1, j)
    # left
    if j - 1 >= 0 and grid[i][j-1] == '1':
        helper(grid, i, j-1)
    # right
    if j + 1 <= len(grid[0])-1 and grid[i][j+1] == '1':
        helper(grid, i, j+1)

input = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(numIslands(input))
