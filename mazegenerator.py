from PIL import Image

# put imgname equal to the image to be solved

imgname = "maze1.png"

def array():

    print("Loading Image")

    image = Image.open(imgname)

    print("Loaded Image")

    width, height = image.size
    

    string = ''
    maze = []

    for i in range(width):
        
        line = ''
        row = []
        
        for j in range(height):
            
            if image.getpixel((j,i))[0] == 255:
                
                line += '1  '
                row.append(1)
            
            else:
                
                line += '0  '
                row.append(0)
        
        line += '\n'
        string += line
        maze.append(row)
    
    

    return maze

    # node making algorithm 
    # key --
    # 0 = wall
    # 1 = connecting nodes
    # 2 = nodes
    # 3 = start node
    # 4 = end node
if __name__ == "__main__":
    array()








