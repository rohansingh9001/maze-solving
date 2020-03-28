# maze-solving
A python code for solving a maze input in the form of a image

### Requirements
Python 3+ installed and added to path
PIL library version 6.2.0

## Installation Instructions
Follow the instructions to install Pillow.

ON LINUX:
1. Open terminal.
2. Type `pip3 install pillow`.
    
Follow similar instructions as linux for Mac OS

ON WINDOWS:
1. Open RUN or press - win + r.
2. Enter cmd
3. Type `pip install pillow`

## How to Use:

The program takes in input as an image. PNG format works best.
The image must be purely black and white i.e. pixel values must read (0,0,0) for black and (255,255,255) for white pixels.
The walls should be black in colour and path should be white.

The entry point must be on the top row in the image. So the topmost row should have all black pixels except one,
which will be the entry point and hence a white pixel.

Similar instructions should be followed for the exit point, the exit point is found on the bottom row instead.
Hence only one pixel should be white in the bottom row and all others should be black.

Also provide an padding of black pixels 1 pixel thick on the left and right side of the walls.

See 'maze.png' for an example.

### EXECUTING THE PROGRAM:
The answer highlights the answer path in a blue line. It also marks the entry and exit points with green and red colours respectively.
1. Open Terminal/Command Prompt.
2. Navigate to the directory where the program is saved.
3. TYPE "python solvemaze.py" ON Windows.
4. TYPE "python3 solvemaze.py" ON Linux.
5. The programs forms an image called "answer.png" which contains the answer.
