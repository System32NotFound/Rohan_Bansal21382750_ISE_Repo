import sys

def get_neighbors(maze, y, x):
    """This module checks the neighbors of the cell and returns the values of the cells in these 4 positions of the target cell: up, down, left, right. 
    Returns the value of the cell in position if it's in range; otherwise, it returns a blank whitespace if it's out of range. 
    This module imports the maze (2D array containing the Ruby generated symbols) and the for-loop counter variables x and y.
    This module also exports the neighbor values which are used by the character_generator module (up, down, left, right)."""
    
    if y > 0:
        up = maze[y-1][x]
    else:
        up = ' '
    
    if y < len(maze) - 1:
        down = maze[y+1][x]
    else:
        down = ' '
    
    if x > 0:
        left = maze[y][x-1]
    else:
        left = ' '
    
    if x < len(maze[y]) - 1:
        right = maze[y][x+1]
    else:
        right = ' '
        
    return up, down, left, right


def character_converter(maze, y, x):
    """This module is responsible for converting the character to box-drawing characters. It goes through the neighbors of the cell and based on the characters converts them to box-drawing characters.
    This module imports the maze array and the counter variables, x and y.
    This module exports the character. Since this module is called for in a for-loop, it will return the character each time it's executed in the loop."""
    
    up, down, left, right = get_neighbors(maze, y, x)

    if maze[y][x] == '+':
        if up == '|' and down == '|' and right == '-':
            return '\u2523'  # ┣
        elif up == '|' and left == '-' and right == '-':
            return '\u253B'  # ┻
        elif up == '|' and right == '-':
            return '\u2517'  # ┗ 
        elif up == '|' and left == '-':
            return '\u251B'  # ┛
        elif down == '|' and right == '-':
            return '\u250F'  # ┏
        elif down == '|' and left == '-':
            return '\u2513'  # ┓
        elif up == '|' and down == '|':
            return '\u2503'  # ┃
        elif up == '|' or down == '|':
      	    return '\u257B'  # ╻
        elif left == '-' and right == '-':
            return '\u2501'  # ━
        elif left == '-' or right == '-':
            return '\u2578'  # ╸
    elif maze[y][x] == '|':
        return '\u2503'  # ┃
    elif maze[y][x] == '-':
        return '\u2501'  # ━'
    
    return ' '


def generate_maze(maze):
    """This module is responsible for actually iterating through the array and generating the maze. A new maze is initialized with empty values, 
    these values are then replaced with the converted characters. A nested for-loop is used to iterate through the two dimensions.
    The module imports the maze array which contains the characters that are going to be converted. This array is then passed to the character_converter module along with the counter variables that contain the cell index information.
    The module exports the new_maze array."""
    print(maze)
    new_maze = [[''] * len(row) for row in maze]
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            new_maze[y][x] = character_converter(maze, y, x)
    
    return new_maze


def read_maze(input_filename):
    """This module is responsible for accepting the maze txt output file of the Ruby code and converting it into a 2D array.
    The module imports the input_filename variable, which contains the filename for the input file. This filename is typed in by the user when running the code.
    The module exports the 2D array that contains the character in the maze txt file."""
    
    with open(input_filename, 'r') as file:
        return [list(line.strip()) for line in file]


def save_maze(maze, output_filename):
    """This module is responsible for saving the maze as a txt file. It iterates over each row and converts the list of characters into a string by joining them together without any separator like (','). 
    The concatenated string is then saved as a file with a new line operator after each row so it's saved in the maze format.
    The module imports the maze array and the name that the user would like to save the new maze under."""
    
    with open(output_filename, 'w', encoding='utf-8') as file:
        for row in maze:
            file.write(''.join(row) + '\n')


def print_maze(maze):
    """This module is responsible for printing the maze to the terminal. The purpose of this module is to correctly see the maze since opening it with a word processor as a txt file messes up the format. 
    When printed on the terminal, however, it displays the maze correctly.
    The module imports the maze 2D array."""
    
    for row in maze:
        print(''.join(row))


def main():
    """The module is the main module of the program that brings all the other modules of the program together. 
    It calls upon the other modules as required. It can be considered the master module that runs the program.
    ** Added a check to make sure user has provided two filenames"""
    if len(sys.argv) != 3:
        print("Please provide two filenames (input)(output)")
        sys.exit(1)
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    
    maze = read_maze(input_filename)
    new_maze = generate_maze(maze)
    
    print("Original Maze:")
    print_maze(maze)
    print("\n")
    print("New Maze:")
    print_maze(new_maze)
    
    save_maze(new_maze, output_filename)
    print("\n")
    print(f"New maze saved to {output_filename}")


if __name__ == "__main__":
    main()

