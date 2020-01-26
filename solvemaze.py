from mazegenerator import array

#Obsolete code. No longer in use. BFSsolve.py is used as a replacement code.
#change N according to the dimensions of your image in pixels
N = 12


def printsol(sol):
    for i in sol:
        for j in i:
            print(j,' ',end=' ')
        print('')
def issafe(maze,x,y):
    if x>=0 and x<N and y>=0 and y<N and maze[x][y]==1:
        return True
    else:
        return False
def solvemaze(maze):
    sol=[[0 for j in range(N)] for i in range(N)]

    if solvemazeuntil(maze,0,0,sol)==False:
        print("Tarun is not so Awesome at solving mazes")
        return False
    printsol(sol)
    return True
def solvemazeuntil(maze,x,y,sol):
    if x==N-1 and y==N-1:
        sol[x][y]=1
        return True
    if issafe(maze,x,y)==True:
        sol[x][y]=1
        if solvemazeuntil(maze,x+1,y,sol)==True:
            return True
        if solvemazeuntil(maze,x,y+1,sol)==True:
            return True

        sol[x][y]=0
        return False
maze = array()




solvemaze(maze)

        
    
    
        
    
    
