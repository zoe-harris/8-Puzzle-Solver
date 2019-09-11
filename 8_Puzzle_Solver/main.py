# Zoe Harris, Rachel Lewis
# CSCE405 Artificial Intelligence
# Programming Assignment #1

from search import Search
from node import Node

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
#  For loop converts the string array into integers
for x in range(len(start_state)):
    for y in range(len(start_state)):
        if start_state[x][y] != "X":
            start_state[x][y] = int(start_state[x][y])

goal_state = [
               [g[0], g[1], g[2]],
               [g[3], g[4], g[5]],
               [g[6], g[7], g[8]],
              ]

# For loop converts the string array into integers
for x in range(len(goal_state)):
    for y in range(len(goal_state)):
        if goal_state[x][y] != "X":
            goal_state[x][y] = int(goal_state[x][y])

a = Node(start_state, None, 0)
b = Node(goal_state, None, 0)
s = Search("BFS", start_state, goal_state)
check = s.check_duplicate(a, b)
print("DUPLICATE T/F: " + str(check))

"""
# read in user's preferred search choice - continue prompting until valid choice entered
search_choice = input("Enter preferred search method: (BFS, Misplaced Tiles, Manhattan Distance, or Gaschnig): ")

valid_searches = ["BFS", "Misplaced Tiles", "Manahattan Distance", "Gaschnig"]

while search_choice not in valid_searches:
    search_choice = input("The search method you ented is invalid. Please enter valid search method"
                          "(BFS, Misplaced Tiles, Manhattan Distance, or Gaschnig): ")
"""