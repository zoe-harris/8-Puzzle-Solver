# Zoe Harris, Rachel Lewis
# CSCE405 Artificial Intelligence
# Programming Assignment #1

from search import Search
from node import Node


def convert_int(con):
    for x in range(len(con)):
        if con[x] != "X":
            con[x] = int(con[x])
    return con


def main():
    # make Search object
    search_obj = Search()

    # Read in start and goal states from user
    start_string = input("Enter start state (separate tiles with a space and mark blank tile with an X): ")
    s = start_string.split()

    goal_string = input("Enter goal state (separate tiles with a space and mark blank tile with an X): ")
    g = goal_string.split()

    # Check parities or start and goal states
    if not search_obj.equal_parity(s, g):
        print("The state you entered did not have the same parity. This puzzle is unsolvable.")

    convert_int(s)
    convert_int(g)

    # Store states as 2D lists
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

    # Read in user's preferred search choice - continue prompting until valid choice entered
    search_choice = input("Enter preferred search method: (BFS, Misplaced Tiles, Manhattan Distance, or Gaschnig): ")

    valid_searches = ["BFS", "Misplaced Tiles", "Manahattan Distance", "Gaschnig"]

    # make Search object
    search = Search(search_choice, Node(start_state), Node(goal_state))
    # search.breadth_first_search()

    n = Node(start_state)
    print(search.num_misplaced(n))

    while search_choice not in valid_searches:
        search_choice = input("The search method you ented is invalid. Please enter valid search method"
                              "(BFS, Misplaced Tiles, Manhattan Distance, or Gaschnig): ")

    # Call requested search method on given 8-Puzzle


if __name__ == "__main__":
    main()


