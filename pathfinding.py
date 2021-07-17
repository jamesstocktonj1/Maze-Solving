#path finding file
#replaces parts of main.py and nodetype.py in previous versions
#James Stockton
#16/07/21

from PIL import Image



#returns number of paths from node x, y
#used to determine node type for example if dead end
def numNewPaths(maze_grid, x, y):

    pathCount = 0

    #white (1) is path so sum is number of paths
    pathCount += maze_grid[y][x + 1]
    pathCount += maze_grid[y][x - 1]
    pathCount += maze_grid[y + 1][x]
    pathCount += maze_grid[y - 1][x]

    return pathCount


#returns the coordinates of the number of paths which can be taken from node x, y
def findNextPaths(maze_grid, x, y):

    nextSquares  = []

    #takes a "plus" look around the node x, y

    #if 1 then add that coordinate to the possible paths
    if maze_grid[y][x + 1] == 1:
        nextSquares.append([x + 1, y])

    if maze_grid[y][x - 1] == 1:
        nextSquares.append([x - 1, y])

    if maze_grid[y + 1][x] == 1:
        nextSquares.append([x, y + 1])
    
    if maze_grid[y - 1][x] == 1:
        nextSquares.append([x, y - 1])

    return nextSquares


def loadFromFile(file_name):

    maze_grid = []

    #load image
    img = Image.open(file_name)

    #only loads the black (0) and white (1) pixel data into a single 1D array
    buf = list(img.getdata(0))

    #converts each row into a 2D array
    for y in range(0, img.size[1]):

        maze_grid.append(buf[(y * img.size[1]) : ((y * img.size[1]) + img.size[0])])


    return maze_grid



def getStartCoordinate(maze_grid):

    #returns the only white pixel in the first row
    return [maze_grid[0].index(1), 0]

def getEndCoordinate(maze_grid):

    #get the last row
    y_end = len(maze_grid) - 1

    #returns the only white pixel in the last row
    return [maze_grid[y_end].index(1), y_end]