# Zoe Harris, Rachel Lewis
# CSCE405 Artificial Intelligence
# Programming Assignment #1

# import node.py

class Search:
    def __init__(self, search, start, goal, closed, o_list):
        self.search_type = search  # This string denotes which search method will be used to solve the puzzle
        self.search_start = start  # This list the starting state of the puzzle
        self.search_goal = goal  # This list the solution to the puzzle
        self.closed_list = closed  # This is a list that holds the nodes that have been expanded
        self.open_list = o_list  # This is a list that holds the nodes that need to be expanded

    # This method will determine the parody of the puzzle to determine is it is solvable
    def check_parody(self):
        print("Hey, some parodies are better than the original. Some are too close. Personal opinion, really.")

    # This method creates a node for each viable move & adds the node to the open_list
    def generate_options(self):
        print("I mean we could get coffee, or tea, or a smoothie.")

    # This method checks to see if the current node is located in the closed list. If it is, it is removed from the
    # open_list.
    def check_duplicate(self):
        print("Duplicates are boring. Be original.")

    # This method compares the current node to search_goal.
    def check_solution(self):
        print("Testing 1,2,3.")

    # This method runs the BFS puzzle solver.
    def breadth_first_search(self):
        print("Congrats, you've made it to BFS! If only it were a BLT.")

    # This method runs the misplaced tiles puzzle solver.
    def misplaced_tiles(self):
        print("Misplaced tiles!? How are we supposed to finish the flooring now?!")

    # This method runs the manhattan distance puzzle solver
    def manhattan_distance(self):
        print("Welcome to manhattan distance. The distance to Manhattan 4,376.1 miles. Wait, this isn't what"
              " we're supposed to do? Lame.")

    # This method runs the gaschnig puzzle solver.
    def gaschnig(self):
        print("Welcome to gaschnig. I'm not sure what this is but it sounds cool.")