#create maze files for solved maze
#James Stockton
#17/07/21



from PIL import Image, ImageColor



#creates an image file with the solved path in green
def exportSolvedMaze(maze_grid, filename, solved_path):

    #split file name in order to create new file name
    file_split = filename.split(".")

    #create node filename 
    export_filename = file_split[0] + "_solved." + file_split[1]

    print("Creating " + export_filename + "...")


    #load new image same size as original maze (RGB)
    img_solve = Image.new('RGB', (len(maze_grid[0]), len(maze_grid)))

    #increment through maze
    for y in range(0, len(maze_grid)):

        for x in range(0, len(maze_grid[0])):

            if [x, y] in solved_path:
                img_solve.putpixel((x, y), ImageColor.getrgb("green"))

            #white if path in the mazegrid
            elif maze_grid[y][x] == 1:

                img_solve.putpixel((x, y), ImageColor.getrgb("white"))

    img_solve.save(export_filename)