#import numpy as np

class Cube:
    def __init__(self, name, age):
        self.orientation = {'top_color': 'white', 
                            'front_color': 'red'}
        self.snapshot = {'white': False,
                         'red': False,
                         'blue': False,
                         'orange': False,
                         'green': False,
                         'yellow': False}
        
        #self.cube = np.empty((3*3*3), dtype=object).fill(None)
        self.cube = [None] * 27

    def get_input_colors(self):
        pass
        

    def populate_colors(self, color_string):

        # Since cubies have multiple faces, map these faces into single cubie index of self.cube
        string_index_to_cubie_index_map = {
            0: 1, 1: 1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8,                          # white center
            9: 0, 10: 3, 11: 6, 12: 9, 13: 10, 14: 11, 15: 12, 16: 13, 17: 14,      # green center
            18: 6, 19: 7, 20: 8, 21: 11, 22: 15, 23: 16, 24: 14, 25: 17, 26: 18,    # red center
            27: 8, 28: 5, 29: 2, 30: 16, 31: 19, 32: 20, 33: 18, 34: 21, 35: 22,    # blue center
            36: 2, 37: 1, 38: 0, 39: 20, 40: 23, 41: 9, 42: 22, 43: 24, 44: 12,     # orange center
            45: 14, 46: 17, 47: 18, 48: 13, 49: 25, 50: 21, 51: 12, 52: 24, 53: 22  # yellow center
        }

        # We then need to understand the positions of the indices
        cubie_index_positions = {
            # centers (W, G, R, B, O, Y)
            4: (0, 0, 1), 10: (0, -1, 0), 15: (1, 0, 0), 19: (0, 1, 0), 23: (-1, 0, 0), 25: (0, 0, -1),

            # corners (WGO, WBO, WGR, WRB, YGO, YGR, YRB, YOB)
            0: (-1, -1, 1), 2: (-1, 1, 1), 6: (1, -1, 1), 8: (1, 1, 1), 12: (-1, -1, -1), 14: (1, -1, -1), 
            18: (1, 1, -1), 22: (-1, 1, -1),

            # edges (WO, WG, WB, WR, OG, OR, OY, BR, RY, BO, BY, OY)
            1: (-1, 0, 1), 3: (0, -1, 1), 5: (0, 1, 1), 7: (1, 0, 1), 9: (-1, -1, 0), 11: (1, -1, 0), 
            13: (0, -1, -1), 16: (1, 1, 0), 17: (1, 0, -1), 20: (-1, 1, 0), 21: (0, 1, -1), 24: (-1, 0, -1)
        }

        def get_cubie_type(cubie_index):
            if cubie_index in [4, 10, 15, 19, 23, 25]:
                return 'center'
            elif cubie_index in [0, 2, 6, 8, 12, 14, 18, 22]:
                return 'corner'
            elif cubie_index in [1, 3, 5, 7, 9, 11, 13, 16, 17, 20, 21, 24]:
                return 'edge'
            else:
                raise Exception("Could not determine cubie type!")

        # Nested function to determine normal vector for given input
        def get_face_normal_vec(index):
            if 0 <= index <= 8:
                return (0, 0, 1)
            elif index <= 17:
                return (0, -1, 0)
            elif index <= 26:
                return (1, 0, 0)
            elif index <= 35:
                return (0, 1, 0)
            elif index <= 44:
                return (-1, 0, 0)
            elif index <= 53:
                return (0, 0, -1)
            else:
                raise Exception("Got index out of range for face value!")

        # Loop through colors input
        for index, color_char in enumerate(color_string):
            cubie_index = string_index_to_cubie_index_map[index]   # determine index of cubie
            face_norm_vec = get_face_normal_vec(index)             # determine which way color faces
            cubie_pos = cubie_index_positions[cubie_index]         # determine position of cubie

            # Update correct cubie to have that color included
            if self.cube[cubie_index] is None:
                # Cubie does not have any values filled yet
                self.cube[cubie_index] = Cubie(square_type=get_cubie_type(cubie_index), pos=cubie_pos, colors={color_char: face_norm_vec})
            else:
                # The cubie is partially filled, so update it
                self.cube[cubie_index].colors[color_char] = face_norm_vec


    def initialize_cube(self):
        default = str(input("Is the cube already solved? (Y/N): "))

        if default[0].upper() == 'Y':
            color_string = "W"*9 + "G"*9 + "R"*9 + "B"*9 + "O"*9 + "Y"*9

        else:
            color_string = self.get_input_colors()

        self.populate_colors(color_string=color_string)

        print(self.cube)



# TODO: Incorporate Cubie class instead of dictionaries
class Cubie:
    """
    Represents an individual square on the cube (27 total on a cube).

    @param square_type: center, corner, or edge
    @param pos: actual location of the Cubie [(-1, -1, -1), ..., (1, 1, 1)]
    @param colors: dictionary of {color: normal_vector}
    """
    def __init__(self, square_type, pos, colors):
        self.square_type = square_type
        self.pos = pos
        self.colors = colors

c1 = Cube("Alex", 12)

c1.initialize_cube()
