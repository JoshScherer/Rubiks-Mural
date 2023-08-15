import numpy as np
import math

class Cube:
    def __init__(self):
        self.cube = [None] * 26  # array of cubies that represent the whole cube

        # String input to cubie index mapping
        self.string_index_to_cubie_index_map = {
            0: 0, 1: 1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8,                          # white center
            9: 0, 10: 3, 11: 6, 12: 9, 13: 10, 14: 11, 15: 12, 16: 13, 17: 14,      # green center
            18: 6, 19: 7, 20: 8, 21: 11, 22: 15, 23: 16, 24: 14, 25: 17, 26: 18,    # red center
            27: 8, 28: 5, 29: 2, 30: 16, 31: 19, 32: 20, 33: 18, 34: 21, 35: 22,    # blue center
            36: 2, 37: 1, 38: 0, 39: 20, 40: 23, 41: 9, 42: 22, 43: 24, 44: 12,     # orange center
            45: 14, 46: 17, 47: 18, 48: 13, 49: 25, 50: 21, 51: 12, 52: 24, 53: 22  # yellow center
        }

        # Positions of each index in the array
        self.cubie_index_positions = {
            # centers (W, G, R, B, O, Y)
            4: (0, 0, 1), 10: (0, -1, 0), 15: (1, 0, 0), 19: (0, 1, 0), 23: (-1, 0, 0), 25: (0, 0, -1),

            # corners (WGO, WBO, WGR, WRB, YGO, YGR, YRB, YOB)
            0: (-1, -1, 1), 2: (-1, 1, 1), 6: (1, -1, 1), 8: (1, 1, 1), 12: (-1, -1, -1), 14: (1, -1, -1), 
            18: (1, 1, -1), 22: (-1, 1, -1),

            # edges (WO, WG, WB, WR, OG, OR, OY, BR, RY, BO, BY, OY)
            1: (-1, 0, 1), 3: (0, -1, 1), 5: (0, 1, 1), 7: (1, 0, 1), 9: (-1, -1, 0), 11: (1, -1, 0), 
            13: (0, -1, -1), 16: (1, 1, 0), 17: (1, 0, -1), 20: (-1, 1, 0), 21: (0, 1, -1), 24: (-1, 0, -1)
        }

    def get_cubie_type(self, cubie_index):
        """
        Gives the type of cubie (center, corner, or edge) based on index in cube array.

        Note: this is a nested function
        """
        if cubie_index in [4, 10, 15, 19, 23, 25]:
            return 'center'
        elif cubie_index in [0, 2, 6, 8, 12, 14, 18, 22]:
            return 'corner'
        elif cubie_index in [1, 3, 5, 7, 9, 11, 13, 16, 17, 20, 21, 24]:
            return 'edge'
        else:
            raise Exception("Could not determine cubie type!")
            
    def get_face_normal_vec(self, index):
        """
        Returns the normal vector for the face color based on index from input

        Note: this is a nested function
        """

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


    def get_input_colors(self):
        # Order for each side (listed first) as FRONT, LEFT, RIGHT, TOP
        orient_order = [['WHITE', 'GREEN', 'BLUE', 'ORANGE'],
                        ['GREEN', 'ORANGE', 'RED', 'WHITE'],
                        ['RED', 'GREEN', 'BLUE', 'WHITE'],
                        ['BLUE', 'RED', 'ORANGE', 'WHITE'],
                        ['ORANGE', 'BLUE', 'GREEN', 'WHITE'],
                        ['YELLOW', 'GREEN', 'BLUE', 'RED']]
        
        full_input = ""
        
        for row in orient_order:
            print("-"*50)
            print("ORIENT: {} ON FRONT, {} ON LEFT, {} ON RIGHT, AND {} UP".format(*row))

            full_input += str(input(f"Provide colors for side with {row[0]} center starting at top left working to bottom right (W/G/R/B/O/Y): "))

        return full_input


    def populate_colors(self, color_string):   
        # Loop through colors input
        for index, color_char in enumerate(color_string):
            cubie_index = self.string_index_to_cubie_index_map[index]   # determine index of cubie
            face_norm_vec = self.get_face_normal_vec(index)             # determine which way color faces
            cubie_pos = self.cubie_index_positions[cubie_index]         # determine position of cubie

            # Update correct cubie to have that color included
            if self.cube[cubie_index] is None:
                # Cubie does not have any values filled yet
                self.cube[cubie_index] = Cubie(square_type=self.get_cubie_type(cubie_index), pos=cubie_pos, colors={color_char: face_norm_vec})
            else:
                # The cubie is partially filled, so update it
                self.cube[cubie_index].colors[color_char] = face_norm_vec


    def initialize_cube(self):
        """
        Initialize the Cubie objects and populate the cube array
        """ 
        default = str(input("Is the cube already solved? (Y/N): "))

        if default[0].upper() == 'Y':
            color_string = "W"*9 + "G"*9 + "R"*9 + "B"*9 + "O"*9 + "Y"*9

        else:
            color_string = self.get_input_colors()

        self.populate_colors(color_string=color_string)


    def visualize_cube(self):  
        positions_to_cubie_index = {v: k for k, v in self.cubie_index_positions.items()}  # 1:1 mapping, so this works

        # 1:many mapping, so we must use the following
        cubie_index_to_string_index_map = {}
        for k, v in self.string_index_to_cubie_index_map.items():
            cubie_index_to_string_index_map[v] = cubie_index_to_string_index_map.get(v, []) + [k]

        output_str = ['*'] * 54

        for cubie in self.cube:
            # Get the position and cubie index for this cubie
            cubie_position = cubie.pos
            cubie_index = positions_to_cubie_index[cubie_position]

            # Place each face in the correct string index
            possible_string_indices = cubie_index_to_string_index_map[cubie_index]

            for color_char, face_norm_vec in cubie.colors.items():
                # Use face norm to select the correct index
                if face_norm_vec == (0, 0, 1):
                    # index must be between 0 and 8
                    index_matching_cond = [ind for ind in possible_string_indices if 0 <= ind <= 8]
                elif face_norm_vec == (0, -1, 0):
                    # index must be between 9 and 17
                    index_matching_cond = [ind for ind in possible_string_indices if 9 <= ind <= 17]
                elif face_norm_vec == (1, 0, 0):
                    # index must be between 18 and 26
                    index_matching_cond = [ind for ind in possible_string_indices if 18 <= ind <= 26]
                elif face_norm_vec == (0, 1, 0):
                    # index must be between 27 and 35
                    index_matching_cond = [ind for ind in possible_string_indices if 27 <= ind <= 35]   
                elif face_norm_vec == (-1, 0, 0):
                    # index must be between 36 and 44
                    index_matching_cond = [ind for ind in possible_string_indices if 36 <= ind <= 44]
                elif face_norm_vec == (0, 0, -1):
                    # index must be between 45 and 53
                    index_matching_cond = [ind for ind in possible_string_indices if 45 <= ind <= 53]
                else:
                    raise Exception("Got an unexpected face normal vector!")
                
                # We should only get ONE possible match with this criteria
                assert len(index_matching_cond) == 1

                correct_index = index_matching_cond[0]
                output_str[correct_index] = color_char

        print("".join(output_str))

    
    def perform_move(self, transformation_matrix, x=None, y=None, z=None):
        """
        Given a transformation matrix for (U, D, R, L, F, or B - or associated primes), perform the move on the cube

        @param transformation_matrix: np.array with values for the corresponding rotation done to appropriate cubies
        @param x: if not None (default), then cubies at this x position undergo the transformation
        @param y: if not None (default), then cubies at this y position undergo the transformation
        @param z: if not None (default), then cubies at this z position undergo the transformation
        """
        assert x is not None or y is not None or z is not None, "Move cannot be performed. Provide axis of rotation."

        # pos_ind is the index of the tuple for position (0 for x, 1 for y, 2 for z)
        # pos_val is the value that the position index must be (-1, 0, or 1)
        if x is not None:
            assert y is None and z is None, "Move cannot be performed. Multiple axes of rotation provided."
            pos_ind = 0 
            pos_val = x

        elif y is not None:
            assert x is None and z is None, "Move cannot be performed. Multiple axes of rotation provided."
            pos_ind = 1
            pos_val = y
        else:
            assert x is None and y is None, "Move cannot be performed. Multiple axes of rotation provided."
            pos_ind = 2
            pos_val = z

        for index, cubie in enumerate(self.cube):
            if cubie.pos[pos_ind] == pos_val:
                self.cube[index].pos = tuple([round(x) for x in np.dot(transformation_matrix, cubie.pos)])
            
                for color, normal_vec in self.cube[index].colors.items():
                    self.cube[index].colors[color] = tuple([round(x) for x in np.dot(transformation_matrix, normal_vec)])


    def U_prime(self, degrees):
        """
        Rotates the top face <degrees> counter-clockwise (when facing top face)

        @param degrees: degrees that top will be rotated counter-clockwise
        """

        assert degrees % 90 == 0, "U' rotation must be multiple of 90 degrees!"
        radians = math.radians(degrees)
        rotation_matrix = np.array([[np.cos(radians), -np.sin(radians), 0],
                                    [np.sin(radians), np.cos(radians), 0],
                                    [0, 0, 1]])
        
        self.perform_move(rotation_matrix, z=1)

    def U(self, degrees):
        """
        Rotates the top face <degrees> clockwise (when facing top face)

        @param degrees: degrees that top will be rotated clockwise
        """

        assert degrees % 90 == 0, "U rotation must be multiple of 90 degrees!"
        self.U_prime(-degrees)


    def D_prime(self, degrees):
        """
        Rotates the bottom face <degrees> counter-clockwise (when facing bottom face)

        @param degrees: degrees that bottom will be rotated counter-clockwise
        """

        assert degrees % 90 == 0, "D' rotation must be multiple of 90 degrees!"
        radians = math.radians(degrees)
        rotation_matrix = np.array([[np.cos(radians), np.sin(radians), 0],
                                    [-np.sin(radians), np.cos(radians), 0],
                                    [0, 0, 1]])
        
        self.perform_move(rotation_matrix, z=-1)

    def D(self, degrees):
        """
        Rotates the bottom face <degrees> clockwise (when facing bottom face)

        @param degrees: degrees that bottom will be rotated clockwise
        """

        assert degrees % 90 == 0, "D rotation must be multiple of 90 degrees!"
        self.D_prime(-degrees)


    def R_prime(self, degrees):
        """
        Rotates the right face <degrees> counter-clockwise (when facing right face)

        @param degrees: degrees that right will be rotated counter-clockwise
        """

        assert degrees % 90 == 0, "R' rotation must be multiple of 90 degrees!"
        radians = math.radians(degrees)
        rotation_matrix = np.array([[np.cos(radians), 0, np.sin(radians)],
                                    [0, 1, 0],
                                    [-np.sin(radians), 0, np.cos(radians)]])
        
        self.perform_move(rotation_matrix, y=1)

    def R(self, degrees):
        """
        Rotates the right face <degrees> clockwise (when facing right face)

        @param degrees: degrees that right will be rotated clockwise
        """

        assert degrees % 90 == 0, "R rotation must be multiple of 90 degrees!"
        self.R_prime(-degrees)


    def L_prime(self, degrees):
        """
        Rotates the left face <degrees> counter-clockwise (when facing left face)

        @param degrees: degrees that left will be rotated counter-clockwise
        """

        assert degrees % 90 == 0, "L' rotation must be multiple of 90 degrees!"
        radians = math.radians(degrees)
        rotation_matrix = np.array([[np.cos(radians), 0, -np.sin(radians)],
                                    [0, 1, 0],
                                    [np.sin(radians), 0, np.cos(radians)]])
        
        self.perform_move(rotation_matrix, y=-1)

    def L(self, degrees):
        """
        Rotates the left face <degrees> clockwise (when facing left face)

        @param degrees: degrees that left will be rotated clockwise
        """

        assert degrees % 90 == 0, "L rotation must be multiple of 90 degrees!"
        self.L_prime(-degrees)

    def F_prime(self, degrees):
        """
        Rotates the front face <degrees> counter-clockwise (when facing front face)

        @param degrees: degrees that front face will be rotated counter-clockwise
        """

        assert degrees % 90 == 0, "F' rotation must be multiple of 90 degrees!"
        radians = math.radians(degrees)
        rotation_matrix = np.array([[1, 0, 0],
                                    [0, np.cos(radians), -np.sin(radians)],
                                    [0, np.sin(radians), np.cos(radians)]])
        
        self.perform_move(rotation_matrix, x=1)

    def F(self, degrees):
        """
        Rotates the front face <degrees> clockwise (when facing front face)

        @param degrees: degrees that front will be rotated clockwise
        """

        assert degrees % 90 == 0, "F rotation must be multiple of 90 degrees!"
        self.F_prime(-degrees)

    def B_prime(self, degrees):
        """
        Rotates the back face <degrees> counter-clockwise (when facing back face)

        @param degrees: degrees that back face will be rotated counter-clockwise
        """

        assert degrees % 90 == 0, "B' rotation must be multiple of 90 degrees!"
        radians = math.radians(degrees)
        rotation_matrix = np.array([[1, 0, 0],
                                    [0, np.cos(radians), np.sin(radians)],
                                    [0, -np.sin(radians), np.cos(radians)]])
        
        self.perform_move(rotation_matrix, x=-1)

    def B(self, degrees):
        """
        Rotates the back face <degrees> clockwise (when facing back face)

        @param degrees: degrees that back will be rotated clockwise
        """

        assert degrees % 90 == 0, "B rotation must be multiple of 90 degrees!"
        self.B_prime(-degrees)




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

c1 = Cube()

c1.initialize_cube()
print("BEFORE:", end=" ")
c1.visualize_cube()

c1.L_prime(90)
c1.L(90)
c1.R(90)
c1.R_prime(90)
c1.F_prime(90)
c1.F(90)
c1.B_prime(90)
c1.B(90)

print("AFTER:", end=" ")
c1.visualize_cube()

