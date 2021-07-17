#path reduction algorithm
#helps reduce the complexity of the maze for the solving algorithm to be run next
#James Stockton
#12/07/21

from pathfinding import *




def deleteToNode(maze_grid, x, y):

    #array of the different squares to delet
    listToDelete = [[x, y]]


    atNode = False

    #repeats until finds a node
    while not atNode:

        #get the previous coord
        prevSquare = listToDelete[len(listToDelete) - 1]

        #if greater than two then must be node
        if numNewPaths(maze_grid, prevSquare[0], prevSquare[1]) > 2:

            #return delete list
            return listToDelete

        else:

            #get next paths 
            nextSquare = findNextPaths(maze_grid, prevSquare[0], prevSquare[1])


            #if not the first node in the array then delete the previous square
            if len(listToDelete) != 1:

                nextSquare.remove(listToDelete[len(listToDelete) - 2])


            #if the node isnt caught then this error message will display
            if len(nextSquare) > 1:

                print("REDUCTION ERROR\nThere are more than one squares to reduce")

            #add the next square to list to delet
            listToDelete.append(nextSquare[0])


def path_reduction(maze_grid, node_grid, maze_size):


    for y in range(1, maze_size[1] - 1):

        for x in range(1, maze_size[0] - 1):

            #if dead end then start reduction
            if node_grid[y][x] == "D":
                delSquares = deleteToNode(node_grid, x, y)

                #print(delSquares)

                if len(delSquares) != 0:
                    for sq in delSquares:

                        #set square to delete to 0 (black)
                        maze_grid[sq[1]][sq[0]] = 0

    return maze_grid