def recurseNumIslands(grid):
    checked = set()
    numIslands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            elevation = grid[row][col]
            if elevation == "1" and not (row, col) in checked:
                numIslands += 1
                
                def dfs(elevationCoords):
                    row, col = elevationCoords
                    elevation = grid[row][col]
                    if elevation == "0" or elevationCoords in checked:
                        return
                    checked.add(elevationCoords)
                    if 0 <= (row - 1):
                        dfs((row - 1, col),)
                    if (row + 1) < len(grid):
                        dfs((row + 1, col),)
                    if 0 <= (col - 1):
                        dfs((row, col - 1),)
                    if (col + 1) < len(grid[0]):
                        dfs((row, col + 1),)

                dfs((row, col),)
    return numIslands

def iterateNumIslands(grid):
    checked = set()
    numIslands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            elevation = grid[row][col]
            if elevation == "1" and not (row, col) in checked:
                numIslands += 1
                
                def idfs(elevationCoords):
                    #implement Iterative DFS
                    pass

                idfs((row, col),)
    return numIslands

def bfsNumIslands(grid):
    checked = set()
    numIslands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            elevation = grid[row][col]
            if elevation == "1" and not (row, col) in checked:
                numIslands += 1
                
                def bfs(elevationCoords):
                    #implement BFS
                    pass
                
                bfs((row, col),)
    return numIslands

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(recurseNumIslands(grid))