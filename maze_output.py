import sys

def cell_character(maze, i, j):
    """Logic to create position checks. Return the value of the cell in position if its in range else it return blank whitespace if its out of range. eg checking for above cell on index [0][y]"""
    if i > 0:
        up = maze[i-1][j]
    else:
        up = ' '
    
    if i < len(maze) - 1:
        down = maze[i+1][j]
    else:
        down = ' '
    
    if j > 0:
        left = maze[i][j-1]
    else:
        left = ' '
    
    if j < len(maze[i]) - 1:
        right = maze[i][j+1]
    else:
        right = ' '
        
        ''' If satements to decide what symbol gets put down by checking the neighbors'''
        
    if maze[i][j] == '+':
        if up == '|' and down == '|' and left == '-' and right == '-':
            return '\u2523'  # ┣
        elif up == '|' and down == '|' and left == '-':
            return '\u2503'  # ┃
        elif up == '|' and down == '|' and right == '-':
            return '\u2523'  # ┣
        elif up == '|' and left == '-' and right == '-':
            return '\u253B'  # ┻
        elif down == '|' and left == '-' and right == '-':
            return '\u253B'  # ┻
        elif up == '|' and right == '-':
            return '\u2517'  # ┗ 
        elif up == '|' and left == '-':
            return '\u251B'  # ┛
        elif down == '|' and right == '-':
            return '\u250F'  # ┏
        elif down == '|' and left == '-':
            return '\u2513'  # ┓
        elif up == '|' or down == '|':
            return '\u2503'  # ┃
        elif left == '-' or right == '-':
            return '\u2501'  # ━
    elif maze[i][j] == '|':
        return '\u2503'  # ┃
    elif maze[i][j] == '-':
        return '\u2501'  # ━
    
    return ' '

def generate_maze(maze):
    """Generate the Maze using for loops to iterate through the 2d array."""
    new_maze = [[''] * len(row) for row in maze]
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            new_maze[i][j] = cell_character(maze, i, j)
    return new_maze

def read_maze(file_path):
    """Read the maze from txt file of ruby code."""
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]

def save_maze(maze, file_path):
    """Save the new maze as txt file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        for row in maze:
            file.write(''.join(row) + '\n')

def print_maze(maze):
    """Print the maze."""
    for row in maze:
        print(''.join(row))

def main():

    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    maze = read_maze(input_file)
    new_maze = generate_maze(maze)
    
    print("Original Maze:")
    print_maze(maze)
    print("\n")
    print("New Maze:")
    print_maze(new_maze)
    
    save_maze(new_maze, output_file)
    print("\n")
    print(f"New maze saved to {output_file}")

if __name__ == "__main__":
    main()
