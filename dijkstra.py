#main Dijkstra's solve algorithm
#James Stockton
#11/07/21


from pathfinding import *


MAX_PATH_LEN = 2000


#main Dijkstra solve algorithm
def solve_maze(maze_grid):

    print("Starting Dijkstra Solve...")

    #calculate start and end point
    start_coord = getStartCoordinate(maze_grid)
    end_coord = getEndCoordinate(maze_grid)

    paths = []
    pathLength = 1

    #create start path with the start coordinate
    paths.append([start_coord, [start_coord[0], start_coord[1] + 1]])

    print(paths)

    #main path finding loop
    while True:

        new_paths = []

        for path in paths:

            #load the last coordinate in the current path
            prevCoord = path[len(path) - 1]

            #get number of possible next paths (- 1 takes away current square)
            numPaths = numNewPaths(maze_grid, prevCoord[0], prevCoord[1]) - 1

            print("New Paths: " + str(numPaths))

            #if no available paths then dont add to new_paths
            if numPaths != 0:

                #find the next possible (including current coord)
                nextPath = findNextPaths(maze_grid, prevCoord[0], prevCoord[1])

                #remove the square last in the path
                nextPath.remove(path[len(path) - 2])


                #if the end coordinate is in the next paths then maze solved
                if end_coord in nextPath:

                    #return solved path
                    return path + [end_coord]


                for n in nextPath:

                    #add the current path in addition to the possible next paths
                    new_paths.append(path + [n])

                    print("New Path")

        
        pathLength += 1

        #print("Path Length: " + str(pathLength))

        #use the new paths for the next iteration
        paths = new_paths



