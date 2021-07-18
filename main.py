
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

    
    #load maze from image
    mazeGrid = loadFromFile(mazeFilename)

    #perform reduction algorithm (optional)
    reducedMaze = path_reduction(mazeGrid)
    exportMazeReduction(reducedMaze, mazeFilename)

    

    startTime = time.time()



    #solve maze depending on file imported (see top)
    #solvedPath = solve_maze(mazeGrid)
    solvedPath = solve_maze(reducedMaze)


    endTime = time.time()

    print("Solve Time: " + str(endTime - startTime))

    exportSolvedMaze(mazeGrid, mazeFilename, solvedPath)


   



