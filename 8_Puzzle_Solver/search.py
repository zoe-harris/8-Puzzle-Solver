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


""" VARIABLES:

     
     METHODS
     check_parody  # This method will determine the parody of the puzzle to determine is it is solveable
     generate_options  # This method creates a node for each viable move & adds the node to the open_list
     check_duplicate  # This method checks to see if the current node is located in the closed list. If it is, it is
      removed from the open_list.
     check_solution  # This method compares the current node to search_goal.
     breadth_first_search  # This method runs the BFS puzzle solver.
     """
