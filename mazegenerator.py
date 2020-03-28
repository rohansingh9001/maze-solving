from PIL import Image


# Set imgname to the value intended to be converted into a matrix
imgname = 'maze2.png'


# put imgname equal to the image to be solved


def array(imgname):

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

            if image.getpixel((j, i))[0] == 255:

                line += '1  '
                row.append(1)
            else:

                line += '0  '
                row.append(0)

        line += '\n'
        string += line
        maze.append(row)

    print(string)

    print(maze)
    return maze


def generate_answer(imgname, path, start, end):
    answer = Image.open(imgname)
    pixels = answer.load()

    for node in path:
        y, x = node
        pixels[x, y] = (0, 0, 255)

    y, x = start
    pixels[x, y] = (0, 255, 0)

    y, x = end
    pixels[x, y] = (255, 0, 0)

    answer.save('answer.png')


if __name__ == "__main__":
    array(imgname)
