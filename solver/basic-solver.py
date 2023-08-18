import sys
import os

# Ugly code to deal with relative imports across directories
sys.path.insert(0, str(os.getcwd()) + '/cube')

from cube import Cube

def main():
    print("Entering main function")
    test_cube = Cube()

    test_cube.initialize_cube()
    print("BEFORE:", end=" ")
    test_cube.visualize_cube()

    test_cube.rotate_cube_along_y_counterclockwise()

    print("AFTER:", end="  ")
    test_cube.visualize_cube()


if __name__ == '__main__':
    main()
