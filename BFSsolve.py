from mazegenerator import array #import the fuction that generates a matrix of the picture


maze = array() #generate the matrix 


#define a function to print the maze in easily readable format (debugging purpose)
# for eg 
#       1  2  3  4  5  6  7  8  9  0
#       1  2  3  4  5  6  7  8  9  0
#       1  2  3  4  5  6  7  8  9  0
#       1  2  3  4  5  6  7  8  9  0
#       1  2  3  4  5  6  7  8  9  0
#       1  2  3  4  5  6  7  8  9  0
#       1  2  3  4  5  6  7  8  9  0
#       1  2  3  4  5  6  7  8  9  0
#       1  2  3  4  5  6  7  8  9  0
#       1  2  3  4  5  6  7  8  9  0
def printmaze(maze):
    for i in maze:
        line = [str(j) for j in i]
        print('  '.join(line))
    print("\n\n\n")

#Define a Node class which will represent each walkable "pixel"
#Attributes are created with respect to the BFS and DFS algorithms
class Node():

    def __init__(self, x, y, nodetype, i):
        
        #The x, y position of the 
        self.x = x
        self.y = y

        #The connected node to this node will contain Node type objects
        self.connected = []

        #Node type key --
        #Nodes are classified as four types
        # 0 = wall i.e. black pixels (Will not end up as nodes as it will waste resources)
        # 1 = connecting nodes or path node i.e. white pixels
        # 2 = start node i.e. the only white pixel in the top most row
        # 3 = end node i.e. the only white pixel in the bottom most row
        self.nodetype = nodetype

        #Also provided a coordinate for ease of access later
        self.coordinates = (x,y)

        #The index number of the Node not used in actual algorithm (Debugging purpose)
        self.index = i
    
    #A function to print the node (Debugging purpose)
    def __str__(self):
        return f"node number {self.index} at {self.coordinates} of type {self.nodetype}"

#Defined a simple Queue Data structure from lists for ease later in BFS algorithm
class Queue():

    def __init__(self):
        self.queue = []

    def new(self, val):
        self.queue.append(val)

    def clear(self):
        self.queue.pop(0)

    def next(self):
        return self.queue[0]

#For a non destructive workflow, a new matrix called nodemaze is created
nodemaze = maze

#Not in use function, may use later
# def calcnodes():   
#     global nodemaze
#     for i in range(len(maze)):
#         for j in range(len(maze)):
#             try:         
#                 if maze[i][j] == 1 and ((maze[i-1][j] == 1 and maze[i][j-1] == 1) or (maze[i-1][j] == 1 and maze[i][j+1] == 1) or (maze[i+1][j] == 1 and maze[i][j-1] == 1) or (maze[i+1][j] == 1 and maze[i][j+1] == 1)):
#                     nodemaze[i][j] = 2
#                 if maze[i][j] == 1 and ((maze[i-1][j] == 1 and maze[i][j-1] == 1 and maze[i+1][j] == 1) or (maze[i-1][j] == 1 and maze[i][j+1] == 1 and maze[i+1][j] == 1) or (maze[i-1][j] == 1 and maze[i][j-1] == 1 and maze[i][j+1] == 1) or (maze[i][j+1] == 1 and maze[i][j-1] == 1 and maze[i+1][j] == 1)):
#                     nodemaze[i][j] = 2
#                 if maze[i][j] == 1 and (maze[i-1][j] == 1 and maze[i+1][j] == 1 and maze[i][j-1] == 1 and maze[i][j+1] == 1):
#                     nodemaze[i][j] = 2
#             except:
#                 pass  
#    printmaze(nodemaze)

#Setup variables to be used in the next function 
start = 0
end = 0
#Detects the start and the end nodes by looping through the first and the last row
def extremenodes():
    global nodemaze
    global start
    global end

    firstline = nodemaze[0]
    lastline = nodemaze[-1]

    for i in range(len(firstline)):
        if firstline[i] == 1:
            nodemaze[0][i] = 2
            start = (0,i)
    for i in range(len(lastline)):
        if lastline[i] == 1:
            nodemaze[-1][i] = 3
            end = (len(nodemaze)-1,i)
    printmaze(nodemaze)

#Create a dictionary for all the nodes, uses the format -- 
#[ coordinates (x,y) : Node object ] -- as each key value pair
nodes = {}

#adds nodes to the node dictionary in the format -- (x,y) : Node
#checks for 1, 2, 3 type nodes in the matrix
def addnodes():
    global nodes
    
    l = 1

    for i in range(len(nodemaze)):
        
        for j in range(len(nodemaze)):
            
            if nodemaze[i][j] == 1:
                nodes[(i, j)] = Node(i, j, 1, l)
                l += 1
            
            if nodemaze[i][j] == 2:
                nodes[(i, j)] = Node(i, j, 2, l)
                l += 1
            
            if nodemaze[i][j] == 3:
                nodes[(i, j)] = Node(i, j, 3, l)
                l += 1

#adds nearby nodes to the connected nodes list. Checks the Upper, Bottom, left and right nodes for presence of
#1, 2, 3 type nodes
def connectednodes():

    for coord, node in nodes.items():
        if node.nodetype == 1 or 2 or 3:
            x,y = coord
            if (x-1,y) in nodes.keys():
                node.connected.append((x-1,y))
            if (x+1,y) in nodes.keys():
                node.connected.append((x+1,y))
            if (x,y-1) in nodes.keys():
                node.connected.append((x,y-1))
            if (x,y+1) in nodes.keys():
                node.connected.append((x,y+1)) 

#Solves the maze using the BFS algorithm.

def bfs():
    
    explored = []
    queue = Queue()
    priority = nodes[start]

    def explore(priority):
        for connected_node in priority.connected:
            if nodes[connected_node].nodetype == 3:
                pathfound == True 
            if connected_node not in explored:
                explored.append(connected_node)
            if connected_node not in queue.queue:
                queue.new(connected_node)
    print(type(priority))
    queue.new(priority)
    explore(priority)
    queue.clear()

    pathfound = False

    while not pathfound:
        priority = queue.next()
        explore(priority)
        queue.clear()
        print(priority)
        print(queue)
    print(explored)
    
#Define the main function 
def main():
    
    extremenodes()
    addnodes()
    connectednodes()
    bfs()

#Execute the main function
if __name__ == "__main__":
    main()











