import unittest
import os
import io
import sys
from maze_output import (
    get_neighbors,
    character_converter,
    generate_maze,
    read_maze,
    save_maze,
    print_maze,
    main
)

class TestMazeGenerator(unittest.TestCase):
    def setUp(self):
        self.sample_maze = [['+', '-', '+', '-', '+', '-', '+', '-', '+', '-', '+', '-', '+', '-', '+', '-', '+', '-', '+', '-', '+'], ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'], ['+', ' ', '+', '-', '+', ' ', '+', ' ', '+', '-', '+', '-', '+', '-', '+', ' ', '+', ' ', '+', ' ', '+'], ['|', ' ', '|', ' ', ' ', ' ', '|', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', '|'], ['+', '-', '+', '-', '+', ' ', '+', ' ', '+', '-', '+', ' ', '+', ' ', '+', ' ', '+', '-', '+', ' ', '+'], ['|', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', ' ', ' ', ' ', '|'], ['+', ' ', '+', '-', '+', ' ', '+', '-', '+', ' ', '+', '-', '+', ' ', '+', '-', '+', '-', '+', ' ', '+'], ['|', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|'], ['+', '-', '+', '-', '+', ' ', '+', ' ', '+', ' ', '+', ' ', '+', ' ', '+', ' ', '+', '-', '+', ' ', '+'], ['|', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', ' ', ' ', '|'], ['+', '-', '+', '-', '+', '-', '+', '-', '+', '-', '+', '-', '+', '-', '+', '-', '+', '-', '+', '-', '+']]


    def test_read_maze(self):
        # Valid filepath
        with open('maze_input.txt', 'w') as f:
            f.write("+-+\n| |\n-+-\n")
        result = read_maze('maze_input.txt')
        self.assertEqual(result, [list("+-+"), list("| |"), list("-+-")])
        os.remove('maze_input.txt')

        # Invalid filepath
        with self.assertRaises(FileNotFoundError):
            read_maze('nonexistent_maze.txt')

    def test_save_maze(self):
        maze = [list("+-+"), list("| |"), list("-+-")]
        save_maze(maze, 'maze_output.txt')
        self.assertTrue(os.path.exists('maze_output.txt'))
        os.remove('maze_output.txt')

    def test_print_maze(self):
        maze = [list("+-+"), list("| |"), list("-+-")]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_maze(maze)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "+-+\n| |\n-+-\n")

    def test_get_neighbors_blackbox(self):

        # Top left corner
        self.assertEqual(get_neighbors(self.sample_maze, 0, 0), (' ', '|', ' ', '-'))
        # Bottom right corner
        self.assertEqual(get_neighbors(self.sample_maze, 10, 20), ('|', ' ', '-', ' '))
        # Middle Cell
        self.assertEqual(get_neighbors(self.sample_maze, 2, 2), (' ', '|', ' ', '-'))
        # Bottom left corner
        self.assertEqual(get_neighbors(self.sample_maze, 10, 0), ('|', ' ', ' ', '-'))
        # Right Edge
        self.assertEqual(get_neighbors(self.sample_maze, 1, 20), ('+', '+', ' ', ' '))

    def test_get_neighbors_whitebox(self):
        # Test cases from the white box design
        #decided to use a smaller maze for simplicity for complex unit testing.
        maze = [
            ['+', ' ', '+', ' ', '+'],
            ['|', ' ', '|', ' ', '|'],
            ['+', '-', '+', '-', '+']
        ]
        # Enter all if, 1st if:(y > 0), 2nd if:(y<len(maze) – 1), 3rd if: (x>0), 4th if: (x<len(maze[y] - 1) -
        self.assertEqual(get_neighbors(maze, 1, 2), ('+', '+', ' ', ' '))
        # Enter 1st else (not y>0) enter all other if -
        self.assertEqual(get_neighbors(maze, 0, 1), (' ', ' ', '+', '+'))
	#Enter 2nd else (not y < len(maze) – 1) and enter all other if -
        self.assertEqual(get_neighbors(maze, 2, 2), ('|', ' ', '-', '-'))
        # Enter 3rd else (not x>0) and enter all other if -
        self.assertEqual(get_neighbors(maze, 1, 0), ('+', '+', ' ', ' '))
        # Enter 4th else (not x < len(maze[y]) – 1) and enter all other if - 
        self.assertEqual(get_neighbors(maze, 1, 4), ('+', '+', ' ', ' '))
        # Enter 1st and 3rd else and enter 2nd and 4th if - 
        self.assertEqual(get_neighbors(maze, 0, 0), (' ', '|', ' ', ' '))
        # Enter 2nd and 4th else and enter 1st and 2nd if - 
        self.assertEqual(get_neighbors(maze, 2, 4), ('|', ' ', '-', ' '))
        # Enter 1st and 4th else and enter 2nd and 3rd if - 
        self.assertEqual(get_neighbors(maze, 0, 4), (' ', '|', ' ', ' '))
        # Enter 2nd and 3rd else and enter 1st and 4th if - 
        self.assertEqual(get_neighbors(maze, 2, 0), ('|', ' ', ' ', '-'))

    def test_character_converter_blackbox(self):

        # Full Line
        self.assertEqual(character_converter(self.sample_maze, 2, 0), '\u2503')
        # Half Line
        self.assertEqual(character_converter(self.sample_maze, 0, 1), '\u2501')
        # Intersection right
        self.assertEqual(character_converter(self.sample_maze, 8, 0), '\u2523')
        # Intersection up
        self.assertEqual(character_converter(self.sample_maze, 10, 16), '\u253B')
        # Corner
        self.assertEqual(character_converter(self.sample_maze, 10, 20), '\u251B')

    def test_character_converter_whitebox(self):

        # Enter both if
        self.assertEqual(character_converter(self.sample_maze, 8, 0), '\u2523')
        # Enter 1st inner elif
        self.assertEqual(character_converter(self.sample_maze, 8, 2), '\u253B')
        # Enter 2nd inner elif
        self.assertEqual(character_converter(self.sample_maze, 10, 0), '\u2517')
        # Enter 3rd inner elif
        self.assertEqual(character_converter(self.sample_maze, 10, 20), '\u251B')
        # Enter 4th inner elif
        self.assertEqual(character_converter(self.sample_maze, 0, 0), '\u250F')
        # Enter 5th inner elif
        self.assertEqual(character_converter(self.sample_maze, 0, 20), '\u2513')
        # Enter 6th inner elif
        self.assertEqual(character_converter(self.sample_maze, 1, 0), '\u2503')
        # Enter 7th inner elif
        self.assertEqual(character_converter(self.sample_maze, 2, 6), '\u257B')
        # Enter 8th inner elif
        self.assertEqual(character_converter(self.sample_maze, 0, 1), '\u2501')
        # Enter 9th inner elif
        self.assertEqual(character_converter(self.sample_maze, 6, 18), '\u2578')
        # Enter 1st outer elif
        self.assertEqual(character_converter(self.sample_maze, 1, 0), '\u2503')
        # Enter 2nd outer elif
        self.assertEqual(character_converter(self.sample_maze, 0, 1), '\u2501')

    def test_generate_maze(self):
        input_maze = [
            ['+', '-', '+'],
            ['|', ' ', '|'],
            ['+', '-', '+']
        ]
        expected_output = [
            ['\u250F', '\u2501', '\u2513'],
            ['\u2503', ' ', '\u2503'],
            ['\u2517', '\u2501', '\u251B']
        ]
        self.assertEqual(generate_maze(input_maze), expected_output)

    def test_main(self):
        # Create a test input file
        with open('test_input.txt', 'w') as f:
            f.write("+-+\n| |\n+-+\n")

        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Run main with test input and output files
        sys.argv = ['maze_generator.py', 'test_input.txt', 'test_output.txt']
        main()

        sys.stdout = sys.__stdout__

        # Check if output file was created
        self.assertTrue(os.path.exists('test_output.txt'))

        # Clean up
        os.remove('test_input.txt')
        os.remove('test_output.txt')

if __name__ == '__main__':
    unittest.main()
