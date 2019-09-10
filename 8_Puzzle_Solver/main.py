# Zoe Harris, Rachel Lewis
# CSCE405 Artificial Intelligence
# Programming Assignment #1

# read in start and goal states
start_string = input("Enter starting puzzle position (separate tiles with a space and mark blank tile with an X): ")
s = start_string.split()
goal_string = input("Enter goal puzzle position (separate tiles with a space and mark blank tile with an X): ")
g = goal_string.split()

start_state = [
               [s[0], s[1], s[2]],
               [s[3], s[4], s[5]],
               [s[6], s[7], s[8]],
              ]

goal_state = [
               [g[0], g[1], g[2]],
               [g[3], g[4], g[5]],
               [g[6], g[7], g[8]],
              ]

# read in user's preferred search choice - continue prompting until valid choice entered
search_choice = input("Enter preferred search method: (BFS, Misplaced Tiles, Manhattan Distance, or Gaschnig): ")

valid_searches = ["BFS", "Misplaced Tiles", "Manahattan Distance", "Gaschnig"]

while search_choice not in valid_searches:
    search_choice = input("The search method you ented is invalid. Please enter valid search method"
                          "(BFS, Misplaced Tiles, Manhattan Distance, or Gaschnig): ")