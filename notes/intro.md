# General Plan

There are several methods for solving Rubik's cubes.

Right now, I have zero experience...

As I advance through this project, I will update the solve logic to make it more efficient and realistic.

* Implement most basic (and inefficient) Rubik's cube solver algorithms
* Deconstruct image into 3x3 grids composed of the 6 available colors
* Visualize solved result prior to calling the solve function
* Add some type of front-end allowing for UI
* Down the line, create digital version of solvable cubes with instructions

# Basic Solving Algorithm
### Moves:
| Move   | Description                              |
|--------|------------------------------------------|
| **R**  | Rotate the right layer clockwise         |
| **R'** | Rotate the right layer counter-clockwise |
| **L**  | Rotate the left layer clockwise          |
| **L'** | Rotate the left layer counter-clockwise  |
| **U**  | Rotate the top layer clockwise           |
| **U'** | Rotate the top layer counter-clockwise   |
| **F**  | Rotate the front layer clockwise         |
| **F'** | Rotate the front layer counter-clockwise |

## Level-Based Approach
*Most basic approach is to solve the bottom layer, then middle, then top*

1. Choose a centerpiece of any color, c. 
2. Make a cross of c, as shown below:

|       | **c** |       |
|-------|-------|-------|
| **c** | **c** | **c** |
|       | **c** |       |

3. Match colors of all four 

## Youtube Video

There are 6 colors of the cube

Centers cannot be manipulated - they are stationary

Put edges and corner pieces relative to the center

Corners have 3 stickers, edges have 2 colors, center has 1 sticker

Layer by layer method

Yellow on top, white on bottom

First we solve the first layer / bottom layer in 2 steps
1. Create a white cross
2. Solve the corner pieces