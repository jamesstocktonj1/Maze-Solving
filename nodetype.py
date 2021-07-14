#Functions handling square classifications
#29/06/21
#James Stockton


#function returns number of routes in out of node (used to determine node type)
def routeSum(arr):
    sum = 0

    sum += arr[0][1]
    sum += arr[1][0]
    sum += arr[1][2]
    sum += arr[2][1]

    #return number of routes (white squares) in boarder of subsquare
    return sum

#function returns true if wall
def isWall(arr):

    #checks to see if the centre square is black
    return (arr[1][1] == 0)

#function returns true if dead end
def isDeadEnd(arr):
    sum = routeSum(arr)

    # if sum == 1 then dead end
    return (sum == 1)

#function returns true if straight
def isStraight(arr):
    sum = routeSum(arr)

    # if sum == 2 then one square in, one square out
    return (sum == 2)

#function returns true if there are multiple paths (node)
def isNode(arr):
    sum = routeSum(arr)

    # if > 2 then not a dead end and not a straight
    return (sum > 2)




"""
nodeType:
    "W" -   Wall
    "S" -   Straight
    "N" -   Node
    "D" -   Dead End

    "B" -   Maze Start
    "E" -   Maze End
"""
def getNodeType(arr):

    if isWall(arr):
        return "W"

    elif isStraight(arr):
        return "S"

    elif isNode(arr):
        return "N"
    
    elif isDeadEnd(arr):
        return "D"

    else:
        return "X"

