# import the fuction that generates a matrix of the picture
from mazegenerator import array, generate_answer

# Import an image processing library to set images
import PIL

# Handle command line arguments and provide the largest number possible
import sys

# Copy mazes
from copy import deepcopy

# Import queue for BFS algorithm
from collections import deque

# Set imgname to the name of the image to be solved
imgname = 'maze.png'

maze = array(imgname)  # generate the matrix


# Define a function to print the maze in easily readable format (debugging purpose)
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


# Define a Node class which will represent each walkable "pixel"
# Attributes are created with respect to the BFS and DFS algorithms
class Node():

    def __init__(self, x, y, nodetype, i):

        # The x, y position of the node
        self.x = x
        self.y = y

        # The connected node to this node will contain Node type objects
        self.connected = []

        # The cost and set it to be a big number in the beginning.
        self.cost = sys.maxsize

        # Node type key --
        # Nodes are classified as four types
        # 0 = wall i.e. black pixels (Will not end up as nodes as it will waste resources)
        # 1 = connecting nodes or path node i.e. white pixels
        # 2 = start node i.e. the only white pixel in the top most row
        # 3 = end node i.e. the only white pixel in the bottom most row
        self.nodetype = nodetype

        # Also provided a coordinate for ease of access later
        self.coordinates = (x, y)

        # The index number of the Node not used in actual algorithm (Debugging purposes)
        self.index = i

    # A function to print the node (Debugging purpose)
    def __str__(self):
        return f"Node number {self.index} at {self.coordinates} of type {self.nodetype}"


# For a non destructive workflow, a new matrix called nodemaze is created
nodemaze = deepcopy(maze)

# Setup variables to be used in the next function
start = None
end = None


# Detects the start and the end nodes by looping through the first and the last row
def extremenodes():
    global nodemaze
    global start
    global end

    firstline = nodemaze[0]
    lastline = nodemaze[-1]

    for i in range(len(firstline)):
        if firstline[i] == 1:
            nodemaze[0][i] = 2
            start = (0, i)
    for i in range(len(lastline)):
        if lastline[i] == 1:
            nodemaze[-1][i] = 3
            end = (len(nodemaze)-1, i)
    printmaze(nodemaze)


# Create a dictionary for all the nodes, uses the format --
# [ coordinates (x,y) : Node object ] -- as each key value pair
nodes = {}


# adds nodes to the node dictionary in the format -- (x,y) : Node
# checks for 1, 2, 3 type nodes in the matrix
def addnodes():
    global nodes

    index = 1

    for i in range(len(nodemaze)):

        for j in range(len(nodemaze)):

            if nodemaze[i][j] == 1:
                nodes[(i, j)] = Node(i, j, 1, index)
                index += 1

            if nodemaze[i][j] == 2:
                nodes[(i, j)] = Node(i, j, 2, index)
                index += 1

            if nodemaze[i][j] == 3:
                nodes[(i, j)] = Node(i, j, 3, index)
                index += 1


# adds nearby nodes to the connected nodes list. Checks the Upper, Bottom, left and right nodes for presence of
# 1, 2, 3 type nodes
def connectednodes():

    for coord, node in nodes.items():
        if node.nodetype == 1 or 2 or 3:
            x, y = coord
            if (x-1, y) in nodes.keys():
                node.connected.append(nodes[(x-1, y)])
            if (x+1, y) in nodes.keys():
                node.connected.append(nodes[(x+1, y)])
            if (x, y-1) in nodes.keys():
                node.connected.append(nodes[(x, y-1)])
            if (x, y+1) in nodes.keys():
                node.connected.append(nodes[(x, y+1)])


# Solves the maze using the BFS algorithm.
def bfs():

    explored = []
    queue = []
    path = []
    queue.append(nodes[start])
    priority = queue.pop(0)
    priority.cost = 0

    # Forward propagation
    while priority.nodetype != 3:
        print('---------------------------------------------------------------')
        print('Exploring', priority)
        explored.append(priority)
        print("Explored:", [node.index for node in explored])
        print('Cost:', [node.cost for node in explored])
        print('Queue:', [node.index for node in queue])
        for node in priority.connected:
            if node not in explored and node not in queue:
                queue.append(node)
            if node.cost > priority.cost:
                node.cost = priority.cost + 1

        priority = queue.pop(0)

    # Define a function which returns the node with minimum cost
    def optimisation(nodes):
        mincost = nodes[0].cost
        minnode = nodes[0]
        for node in nodes:
            if node.cost < mincost:
                mincost = node.cost
                minnode = node
        return minnode

    print('-------------------------Backtracking---------------------------')
    currentnode = nodes[end]
    # Backtracking
    while currentnode.nodetype != 2:
        print(path)
        minnode = optimisation(currentnode.connected)
        path.append(minnode.coordinates)
        currentnode = minnode

    generate_answer(imgname, path, start, end)


# Define the main function
def main():

    extremenodes()
    addnodes()
    connectednodes()
    bfs()


# Execute the main function
if __name__ == "__main__":
    print('Nodes:', nodes)
    main()
