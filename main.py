
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


mazeFilename = "solve/logo.png"


            

if __name__ == "__main__":

    loadMazeImage("solve/perfect15k.png")

    #setNodeTypes()

    for i in range(0, 40):

        print("Reduction: " + str(i))

        setNodeTypes()

        #perform reduction algorithm
        mazeGrid = path_reduction(mazeGrid, nodeGrid, mazeSize)
    
    
    createReductionImage()


    #solve maze depending on file imported (see top)
    #solvedPath = solve_maze(mazeGrid)
    solvedPath = solve_maze(reducedMaze)


    endTime = time.time()

    print("Solve Time: " + str(endTime - startTime))

    exportSolvedMaze(mazeGrid, mazeFilename, solvedPath)


   



