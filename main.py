
from nodetype import *
from solve import *
from pathredux import *
from PIL import Image, ImageColor

#dijkstra solving algorithm 




"""

V1.1
changes:
    nodeGrid is now an 2D array of chars rather than Node objects which will reduce memory
    therefore node.py file no longer exists


"""



Image.MAX_IMAGE_PIXELS = None

mazeSize = [0, 0]
mazeGrid = []
nodeGrid = []

img_filename = ""

startCoord = [0, 0]
endCoord = [0, 0]




def loadMazeImage(fileName):
    global startCoord, endCoord, img_solve, img_filename

    img_filename = fileName

    #Load Image
    print("Loading file " + fileName + " ...")
    img = Image.open(img_filename)

    mazeSize[0] = img.size[0]           #image width
    mazeSize[1] = img.size[1]           #image height

    buf = list(img.getdata(0))          #converts to list (0 - black, 1 - white)

    #convert buffer to 2D array (mazeGrid[y][x])
    for y in range(0, mazeSize[1]):
        mazeGrid.append(buf[(y * mazeSize[1]):((y * mazeSize[1]) + mazeSize[0])])

        #print(mazeGrid[y])
    
    #print("Maze Size: " + str(mazeSize))

    #find start (simple top row)
    startCoord = [mazeGrid[0].index(1), 0]
    print("Maze Start:" + str(startCoord))

    #find end (simple bottom row)
    endCoord = [mazeGrid[mazeSize[1] - 1].index(1), mazeSize[1] - 1]
    print("Maze End: " + str(endCoord))



#returns a 3x3 array of the area around (x, y)
def getSubsection(x, y):
    arr = []

    arr.append(mazeGrid[y-1][x-1:x+2])
    arr.append(mazeGrid[y][x-1:x+2])
    arr.append(mazeGrid[y+1][x-1:x+2])

    return arr





#sets the nodeGrid with the relevant node types
def setNodeTypes():

    for y in range(mazeSize[1]):
        nodeGrid.append([])

        for x in range(mazeSize[0]):
            nodeGrid[y].append("X")

            if [x, y] == startCoord:
                nodeGrid[y][x] = "B"
                print("Start: " + str([x, y]))

            elif [x, y] == endCoord:
                nodeGrid[y][x] = "E"
                print("End: " + str([x, y]))

            elif (x == 0) or (x == mazeSize[0]-1) or (y == 0) or (y == mazeSize[1]-1):
                nodeGrid[y][x] = "W"
            
            else:
                nodeGrid[y][x] = getNodeType(getSubsection(x, y))





#creates colour coded image of maze square types
def createSolveImageNodeTypes():
    global nodeGrid
    
    #split file name in order to create new file name
    file_split = img_filename.split(".")

    #create node filename 
    node_filename = file_split[0] + "_nodes." + file_split[1]

    print("Creating " + node_filename + "...")

    #load new image same size as original maze (RGB)
    img_solve = Image.new('RGB', (mazeSize[0], mazeSize[1]))

    for y in range(mazeSize[1]):

        for x in range(mazeSize[0]):

            #begining pixel orange
            if nodeGrid[y][x] == "B":
                img_solve.putpixel((x, y), ImageColor.getrgb("orange"))

            #end pixel orange
            elif nodeGrid[y][x] == "E":
                img_solve.putpixel((x, y), ImageColor.getrgb("orange"))

            #straight pixel yellow
            elif nodeGrid[y][x] == "S":
                img_solve.putpixel((x, y), ImageColor.getrgb("yellow"))

            #node pixel green
            elif nodeGrid[y][x] == "N":
                img_solve.putpixel((x, y), ImageColor.getrgb("green"))

            #dead end pixel red
            elif nodeGrid[y][x] == "D":
                img_solve.putpixel((x, y), ImageColor.getrgb("red"))


    #save image and load preview
    img_solve.save(node_filename)
    #img_solve.show()

def createPathImage(solved_path):

    #split file name in order to create new file name
    file_split = img_filename.split(".")

    #create node filename 
    node_filename = file_split[0] + "_solved." + file_split[1]

    print("Creating " + node_filename + "...")

    #load new image same size as original maze (RGB)
    img_solve = Image.new('RGB', (mazeSize[0], mazeSize[1]))


    for c in solved_path:
        img_solve.putpixel((c[0], c[1]), ImageColor.getrgb("green"))



    #for y in range(mazeSize[1]):

        #for x in range(mazeSize[0]):

            #if [x, y] in solved_path:
                #img_solve.putpixel((x, y), ImageColor.getrgb("green"))

            #elif nodeGrid[y][x] != "W":
                #img_solve.putpixel((x, y), ImageColor.getrgb("white"))
    
    #save image and load preview
    img_solve.save(node_filename)
    img_solve.show()


def createReductionImage():

    #split file name in order to create new file name
    file_split = img_filename.split(".")

    #create node filename 
    node_filename = file_split[0] + "_reduction." + file_split[1]

    print("Creating " + node_filename + "...")

    #load new image same size as original maze (RGB)
    img_solve = Image.new('RGB', (mazeSize[0], mazeSize[1]))

    for y in range(mazeSize[1]):

        for x in range(mazeSize[0]):

            if mazeGrid[y][x] == 1:
                img_solve.putpixel((x, y), ImageColor.getrgb("white"))

    #save image and load preview
    img_solve.save(node_filename)



def printNodeTypes():
    
    for y in range(mazeSize[1]):
        print("")

        #for x in range(mazeSize[0]):

        print(nodeGrid[y], end="\t")


            




if __name__ == "__main__":

    loadMazeImage("solve/perfect15k.png")

    #setNodeTypes()

    for i in range(0, 40):

        print("Reduction: " + str(i))

        setNodeTypes()

        #perform reduction algorithm
        mazeGrid = path_reduction(mazeGrid, nodeGrid, mazeSize)
    
    
    createReductionImage()

    setNodeTypes()

    createSolveImageNodeTypes()

    #printNodeTypes()

    #createSolveImageNodeTypes()


    solvedPath = dijkstra_solve(nodeGrid, startCoord, endCoord)
    print("Solved path length: " + str(len(solvedPath)))
    #print(solvedPath)


    createPathImage(solvedPath)



