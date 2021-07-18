#path reduction algorithm
#helps reduce the complexity of the maze for the solving algorithm to be run next
#James Stockton
#12/07/21

from pathfinding import *




def deleteToNode(maze_grid, x, y):

    #array of the different squares to delete
    listToDelete = [[x, y]]


    atNode = False

    #repeats until finds a node
    while not atNode:

        #get the previous coord
        prevSquare = listToDelete[len(listToDelete) - 1]
        nextSquares = findNextPaths(maze_grid, prevSquare[0], prevSquare[1])


        #if not the first node (dead end) then delete previous square to stop repeating
        if len(listToDelete) > 1:

            if listToDelete[len(listToDelete) - 2] in nextSquares:

                nextSquares.remove(listToDelete[len(listToDelete) - 2])


        #if node is not caught then this error will show up
        if len(nextSquares) > 1:
            print("REDUCTION ERROR\nThere are more than one squares to reduce")
        

        #if the next square is a node then return
        if numNewPaths(maze_grid, nextSquares[0][0], nextSquares[0][1]) > 2:
            return listToDelete
        
        #add the next square to the list to delete
        else:
            listToDelete.append(nextSquares[0])


        



def path_reduction(maze_grid):


    for y in range(1, len(maze_grid) - 1):

        for x in range(1, len(maze_grid[0]) - 1):


            #if dead end (and coord x, y is not a wall) then start reduction
            if (numNewPaths(maze_grid, x, y) == 1) and (maze_grid[y][x] == 1):
                
                delSquares = deleteToNode(maze_grid, x, y)

                if len(delSquares) != 0:

                    for sq in delSquares:

                        #set square to delete to 0 (black)
                        maze_grid[sq[1]][sq[0]] = 0

    return maze_grid
