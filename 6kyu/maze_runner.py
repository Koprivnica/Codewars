"""
Welcome Adventurer. Your aim is to navigate the maze and reach the finish point without touching any walls. Doing so will kill you
instantly!

You will be given a 2D array of the maze and an array of directions. Your task is to follow the directions given. If you reach the end
point before all your moves have gone, you should return Finish. If you hit any walls or go outside the maze border, you should return
Dead. If you find yourself still in the maze after using all the moves, you should return Lost.

The Maze array will look like

maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]

..with the following key

      0 = Safe place to walk
      1 = Wall
      2 = Start Point
      3 = Finish Point

  direction = ["N","N","N","N","N","E","E","E","E","E"] == "Finish"

Rules

1. The Maze array will always be square i.e. N x N but its size and content will alter from test to test.

2. The start and finish positions will change for the final tests.

3. The directions array will always be in upper case and will be in the format of N = North, E = East, W = West and S = South.

4. If you reach the end point before all your moves have gone, you should return Finish.

5. If you hit any walls or go outside the maze border, you should return Dead.

6. If you find yourself still in the maze after using all the moves, you should return Lost.
"""


def maze_runner(maze, directions):

    n = len(maze)
    
    # finding starting point(2)
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                row = i
                column = j
                break
    
    # moving through the maze
    for elem in directions:
        if elem == "N":
            row -= 1
        elif elem == "S":
            row += 1
        elif elem == "W":
            column -= 1
        elif elem == "E":
            column += 1
    
        # checking the square
        if row < 0 or row > n-1 or column < 0 or column > n-1 or maze[row][column] == 1:
            return "Dead"
        elif maze[row][column] == 3:
            return "Finish"
    
    return "Lost"



maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]

direction = ["N","N","N","N","N","E","E","S","S","S","S","S","S"]

print(maze_runner(maze, direction))