# Zoe Harris, Rachel Lewis
# CSCE405 Artificial Intelligence
# Programming Assignment #1

from node import Node


class Search:
    def __init__(self, search=None, start=None, goal=None, closed_list=None, open_list=None):
        self.search_type = search  # This string denotes which search method will be used to solve the puzzle
        self.search_start = start  # This list the starting state of the puzzle
        self.search_goal = goal  # This list the solution to the puzzle
        self.closed_list = closed_list  # This is a list that holds the nodes that have been expanded
        self.open_list = open_list  # This is a list that holds the nodes that need to be expanded

    """ This method will determine the parody of the puzzle to determine if it is solvable. """
    def check_parity(self):
        p_s = 0  # parity of the start
        p_g = 0  # parity of the goal

        temp = []
        #  First for-loop determines the parody function of the start of the puzzle.
        for x in range(len(self.search_start)):
            for y in range(len(self.search_start)):
                temp.append(self.search_start[x][y])

        for x in range(0, len(temp)):
            for y in range(x + 1, len(temp)):
                if (temp[x] != "X") and (temp[y] != "X"):
                    if temp[x] > temp[y]:
                        print("Parity", temp[x], " ", temp[y])
                        p_s = p_s + 1

        #  Second for-loop determines the parity function of the goal of the puzzle.
        temp.clear()
        for x in range(len(self.search_goal)):
            for y in range(len(self.search_goal)):
                temp.append(self.search_goal[x][y])
        print()
        for x in range(0, len(temp)):
            for y in range(x + 1, len(temp)):
                if (temp[x] != "X") and (temp[y] != "X"):
                    if temp[x] > temp[y]:
                        print("Parity", temp[x], " ", temp[y])
                        p_g = p_g + 1

        print("Start Parity: ", p_s, "\nGoal Parity: ", p_g)
        if (p_s % 2) == (p_g % 2):
            if p_s % 2 == 0:
                print("Parity is equal and even.")
            else:
                print("Parity is equal and odd.")
        else:
            print("Parity is not equal.")

    """This prints the current puzzle state."""
    def print_state(self, n):

        arr = n.val
        for i in range(3):
            print(arr[i][0] + " " + arr[i][1] + " " + arr[i][2])

    """ This method finds the blank ('X') in the puzzle. """
    def find_blank(self, n):

        index = [0, 0]
        arr = n.val
        for i in range(3):
            for j in range(3):
                if arr[i][j] is 'X':
                    index = [i, j]

        return index

    """ This method expands the current puzzle node. """
    def expand(self, curr_node):

        index = self.find_blank(curr_node)
        x = index[0]
        print("X: " + str(x))
        y = index[1]
        print("Y: " + str(y))
        options = []

        # UP
        if x > 0:
            new_list = curr_node.val.copy()
            new_list[x][y], new_list[x - 1][y] = new_list[x - 1][y], new_list[x][y]
            up = Node(new_list, curr_node, curr_node.g + 1)
            print("UP")
            self.print_state(up)
            options.append(up)
        # DOWN
        if x < 2:
            new_list = curr_node.val.copy()
            new_list[x][y], new_list[x + 1][y] = new_list[x + 1][y], new_list[x][y]
            down = Node(new_list, curr_node, curr_node.g + 1)
            print("DOWN")
            self.print_state(down)
            options.append(down)
        # LEFT
        if y > 0:
            new_list = curr_node.val.copy()
            left = Node(new_list, curr_node, curr_node.g + 1)
            new_list[x][y], new_list[x][y - 1] = new_list[x][y - 1], new_list[x][y]
            print("LEFT")
            self.print_state(left)
            options.append(left)
        # RIGHT
        if y < 2:
            new_list = curr_node.val.copy()
            new_list[x][y], new_list[x][y + 1] = new_list[x][y + 1], new_list[x][y]
            right = Node(new_list, curr_node, curr_node.g + 1)
            print("RIGHT")
            self.print_state(right)
            options.append(right)

        return options

    """ This method checks to see if the current node is located in the closed list. If it is, it is removed from the
    open_list. """
    def check_duplicate(self):
        print("Duplicates are boring. Be original.")

    """ This method compares the current node to search_goal. """
    def check_solution(self, current):
        print("Testing 1,2,3.")
        for x in range(len(self.search_goal)):
            for y in range(len(self.search_goal)):
                if current[x][y] != self.search_goal[x][y]:
                    return False
        return True


    """ This method runs the BFS puzzle solver. """
    def breadth_first_search(self):
        print("Congrats, you've made it to BFS! If only it were a BLT.")

    """ This method runs the misplaced tiles puzzle solver. """
    def misplaced_tiles(self):
        print("Misplaced tiles!? How are we supposed to finish the flooring now?!")

    """ This method runs the manhattan distance puzzle solver. """
    def manhattan_distance(self):
        print("Welcome to manhattan distance. The distance to Manhattan 4,376.1 miles. Wait, this isn't what"
              " we're supposed to do? Lame.")

    """ This method runs the gaschnig puzzle solver. """
    def gaschnig(self):
        print("Welcome to gaschnig. I'm not sure what this is but it sounds cool.")