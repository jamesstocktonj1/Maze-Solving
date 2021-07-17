
#main for Maze Solving algorithm
#James Stockton
#29/06/21

#uncomment for solving algorithm
from dijkstra import *

from exportmaze import *
from pathredux import *
import time
from PIL import Image




Image.MAX_IMAGE_PIXELS = None


mazeFilename = "solve/normal.png"


            

if __name__ == "__main__":

    """
    mazeGrid = loadFromFile(mazeFilename)

    for r in mazeGrid:
        print(r)


    mazeStart = getStartCoordinate(mazeGrid)

    print("Maze Start " + str(mazeStart))

    print("Maze End " + str(getEndCoordinate(mazeGrid)))

    

    print(findNextPaths(mazeGrid, mazeStart[0], mazeStart[1]))

    nextCoord = findNextPaths(mazeGrid, mazeStart[0], mazeStart[1])

    print(numNewPaths(mazeGrid, nextCoord[0][0], nextCoord[0][1]))
    """

    

    #load maze from image
    mazeGrid = loadFromFile(mazeFilename)
    

    startTime = time.time()



    #solve maze depending on file imported (see top)
    solvedPath = solve_maze(mazeGrid)


    endTime = time.time()

    print("Solve Time: " + str(endTime - startTime))

    exportSolvedMaze(mazeGrid, mazeFilename, solvedPath)


   



