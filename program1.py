class Solution:
   def getTotalIsles(self, grid: list[list[str]]) -> int:
    
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 'W':
                return
            grid[r][c] = 'W'  # mark as visited
            # visit all adjacent cells (up, down, left, right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        num_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 'L':
                    num_islands += 1
                    dfs(r, c)
        
        return num_islands              
