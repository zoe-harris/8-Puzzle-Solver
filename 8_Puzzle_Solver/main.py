# Zoe Harris, Rachel Lewis
# CSCE405 Artificial Intelligence
# Programming Assignment #1

from node import Node
from search import Search

# read in start and goal puzzles
start_string = input("Enter starting puzzle position (separate tiles with a space and mark blank tile with an X): ")
goal_string = input("Enter goal puzzle position (separate tiles with a space and mark blank tile with an X): ")

# read in user's preferred search choice - continue prompting until valid choice entered
search_choice = input("Enter preferred search method: (BFS, Misplaced Tiles, Manhattan Distance, or Gaschnig): ")

valid_searches = ["BFS", "Misplaced Tiles", "Manahattan Distance", "Gaschnig"]

while search_choice not in valid_searches:
    search_choice = input("The search method you ented is invalid. Please enter valid search method"
                          "(BFS, Misplaced Tiles, Manhattan Distance, or Gaschnig): ")