





"""
Node type for each square of the grid

coords:
    [x, y]


nodeType:
    "W" -   Wall
    "S" -   Straight
    "N" -   Node
    "D" -   Dead End

    "B" -   Maze Start
    "E" -   Maze End
"""


class Node:

    def __init__(self, coord):

        self.coords = coord
        self.nodeType = None


    def getCoords(self):
        return self.coords


    def getNodeType(self):
        return self.nodeType

    def setNodeType(self, nodeType):
        self.nodeType = nodeType

    
    