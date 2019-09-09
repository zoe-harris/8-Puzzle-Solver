# Zoe Harris, Rachel Lewis
# CSCE405 Artificial Intelligence
# Programming Assignment #1

import node.py

class search:
    def __init__(self, start, goal, closed, open, search):
        test = 0


""" VARIABLES:
    search_start  # This holds the starting state of the puzzle
    search_goal  # This holds the solution to the puzzle
    closed_list  # This is a list that holds the nodes that have been expanded
    open_list  # This is a list that holds the nodes that need to be expanded
    search_type  # This denotes which search method will be used to solve the puzzle
     
     METHODS
     check_parody  # This method will determine the parody of the puzzle to determine is it is solveable
     generate_options  # This method creates a node for each viable move & adds the node to the open_list
     check_duplicate  # This method checks to see if the current node is located in the closed list. If it is, it is
      removed from the open_list.
     check_solution  # This method compares the current node to search_goal.
     breadth_first_search  # This method runs the BFS puzzle solver.
     """
