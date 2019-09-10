# Zoe Harris, Rachel Lewis
# CSCE405 Artificial Intelligence
# Programming Assignment #1

# read in start and goal puzzles
start_string = input("Enter starting puzzle position (separate tiles with a space and mark blank tile with an X): ")
start = start_string.split()
goal_string = input("Enter goal puzzle position (separate tiles with a space and mark blank tile with an X): ")
goal = goal_string.split()

# read in user's preferred search choice - continue prompting until valid choice entered
search_choice = input("Enter preferred search method: (BFS, Misplaced Tiles, Manhattan Distance, or Gaschnig): ")

valid_searches = ["BFS", "Misplaced Tiles", "Manhattan Distance", "Gaschnig"]

while search_choice not in valid_searches:
    search_choice = input("The search method you entered is invalid. Please enter valid search method"
                          "(BFS, Misplaced Tiles, Manhattan Distance, or Gaschnig): ")