#main Dijkstra's solve algorithm
#James Stockton
#11/07/21


import time
#from node import *
#import main


#node grid y, x


#works out the next step(s) in the path
def getNextRoutes(node_grid, curCoord, prevCoord):

    #possible next squares
    valid_paths = ["S", "N", "E"]

    pos_paths = []

    #straight or node is a possible path
    if node_grid[curCoord[1] + 1][curCoord[0]] in valid_paths:
        pos_paths.append([curCoord[0], curCoord[1] + 1])

    if node_grid[curCoord[1] - 1][curCoord[0]] in valid_paths:
        pos_paths.append([curCoord[0], curCoord[1] - 1])

    if node_grid[curCoord[1]][curCoord[0] + 1] in valid_paths:
        pos_paths.append([curCoord[0] + 1, curCoord[1]])

    if node_grid[curCoord[1]][curCoord[0] - 1] in valid_paths:
        pos_paths.append([curCoord[0] - 1, curCoord[1]])

    if prevCoord in pos_paths:
        pos_paths.remove(prevCoord)

    return pos_paths


#main Dijkstra solve algorithm
def dijkstra_solve(node_grid, start_coords, end_coords):

    print("Starting solve...")
    start_time = time.time()

    solved_path = []
    paths = []

    print("Finding path from " + str(start_coords) + " to " + str(end_coords))

    #create start path which is start coord and then first square after
    paths.append([start_coords, [start_coords[0], start_coords[1] + 1]])

    print("Start Path " + str(paths))


    isSolved = False
    pathLength = 2

    while not isSolved:
    #for j in range(0, 22):

        #print(paths)

        new_paths = []

        #iterate through each possible path
        for path in paths:

            nextPath = getNextRoutes(node_grid, path[len(path) - 1], path[len(path) - 2])
            #print("\nNew Paths: " + str(nextPath))

            #no new paths means end of path
            if len(nextPath) == 0:

                #nothing added to new_paths so path ends
                #print("Dead End")
                pass


            #handle end path (SOLUTION!)
            elif end_coords in nextPath:

                end_time = time.time()

                #create final solved path
                solved_path = path + [end_coords]


                print("\nMaze Solved\n")
                print("Time Taken: " + str(end_time - start_time) + " s")

                return solved_path

            #handle continue path
            else:

                for new in nextPath:
                    #print(new)

                    #checks for infinite loops (new square which is already in path)
                    if new not in path:
                        new_paths.append(path + [new])

                    #print("New Path" + str(paths[len(paths) - 1]))

                #print(new_paths)


        #set paths as the newly found paths for next iteration
        paths = new_paths

        pathLength += 1
        if pathLength > 2000:
            return paths[0]

        print("New Paths: " + str(len(paths)))

        #print("Paths: " + str(len(paths)))






