#path reduction algorithm
#helps reduce the complexity of the maze for the solving algorithm to be run next
#James Stockton
#12/07/21

from nodetype import *




def getSubsection(maze_grid, x, y):
    arr = []

    arr.append(maze_grid[y-1][x-1:x+2])
    arr.append(maze_grid[y][x-1:x+2])
    arr.append(maze_grid[y+1][x-1:x+2])

    return arr

#finds out all the connecting squares at x, y  
def getNextSquares(node_grid, x, y):

    #possible next squares
    valid_paths = ["S", "N", "E"]

    pos_paths = []


    if node_grid[y + 1][x] in valid_paths:
        pos_paths.append([x, y + 1])

    if node_grid[y - 1][x] in valid_paths:
        pos_paths.append([x, y - 1])

    if node_grid[y][x + 1] in valid_paths:
        pos_paths.append([x + 1, y])

    if node_grid[y][x - 1] in valid_paths:
        pos_paths.append([x - 1, y])


    return pos_paths


#produces an array of coordinates which can be removed 
#this is from the dead end until the path reaches a node 
#node is not deleted
def deleteToNode(node_grid, x, y):

    #array of the different squares to delete
    listToDelete = [[x,y]]


    atNode = False

    #keeps repeating until it deletes to node
    while not atNode:
    #for i in range(0, 20):

        #get next squares in path
        prevSquare = listToDelete[len(listToDelete) - 1]
        nextSquares = getNextSquares(node_grid, prevSquare[0], prevSquare[1])


        #if not the first square then delete the square before
        if len(listToDelete) > 1:

            if listToDelete[len(listToDelete) - 2] in nextSquares:
                #remove previous square from 
                nextSquares.remove(listToDelete[len(listToDelete) - 2])

        if len(nextSquares) > 1:
            print("REDUCTION ERROR\nThere are more than one squares to reduce")
        
        #if node then stop reduction since path is most reduced
        if node_grid[nextSquares[0][1]][nextSquares[0][0]] == "N":
            return listToDelete

        else:
            listToDelete.append(nextSquares[0])


    return listToDelete
        



        







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
                

