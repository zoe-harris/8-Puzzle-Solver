# Zoe Harris, Rachel Lewis
# CSCE405 Artificial Intelligence
# Programming Assignment #1

from node import Node
from PriorityQueue import PriorityQueue
import copy


class Search:
    def __init__(self, start=None, goal=None):
        self.search_start = start  # This list the starting state of the puzzle
        self.search_goal = goal  # This list the solution to the puzzle
        self.closed_list = []  # This is a list that holds the nodes that have been expanded
        self.open_list = PriorityQueue()  # This is a list that holds the nodes that need to be expanded

    """""""""""""""""""""""""""""""""""""""    CHECK PARITY    """""""""""""""""""""""""""""""""""""""

    """ This method will determine the parity of the puzzle to determine if it is solvable. """
    def equal_parity(self, s, g):

        # Make copies of s and g so that the lists can be manipulated without impacting
        # the rest of the code.
        s_test = copy.deepcopy(s)
        g_test = copy.deepcopy(g)

        # Remove blank space marker.
        s_test.remove('X')
        g_test.remove('X')

        # Start parity counts at zero.
        s_parity = 0
        g_parity = 0

        # Compare each element of the list against all the elements indexed after it, incrementing
        # parity count each time the element is greater than any of the elements indexed after it.
        for i in range(len(s_test)):
            for j in range(i, len(s_test)):
                if s_test[i] > s_test[j]:
                    s_parity += 1
                if g_test[i] > g_test[j]:
                    g_parity += 1

        # Determine whether parities or both equal or both odd; if they are the same return true.
        if (s_parity % 2) == (g_parity % 2):
            return True  # The parities ARE the same
        else:
            return False  # The parities are NOT the same

    """""""""""""""""""""""""""""""""""""""     PRINTING METHODS     """""""""""""""""""""""""""""""""""""""

    """This prints the current puzzle state."""
    def print_state(self, n):
        for x in range(3):
            print(n.val[x][0], n.val[x][1], n.val[x][2])

    """ This method prints the path of the solution. """
    def print_path(self, n):

        path = []

        # Add all predecessors of goal state to path list
        while n.pred is not None:
            path.insert(0, n)
            n = n.pred

        path.insert(0, n)

        # Print each state in path list
        print()
        print("Solution Path:")

        for i in range(len(path)):
            self.print_state(path[i])
            print()

    """""""""""""""""""""""""""""""""""""""     'CHECK' METHODS     """""""""""""""""""""""""""""""""""""""

    """ This method checks to see if the current node is located in the closed list. If it is, it is removed from the
    open_list. """

    def duplicate(self, n):

        duplicate = True

        for i in range(len(self.closed_list)):
            duplicate = True
            for x in range(len(n.val)):
                for y in range(len(n.val)):
                    if n.val[x][y] != self.search_goal.val[x][y]:
                        duplicate = False

        return duplicate

    def check_duplicate(self, n):

        if len(self.closed_list) == 0:
            return False

        duplicate = True

        for x in range(len(self.closed_list)):
            temp = self.closed_list[x]
            duplicate = True

            for i in range(3):
                for j in range(3):
                    if n.val[i][j] is not temp.val[i][j]:
                        duplicate = False

            if duplicate is True:
                return duplicate

        return duplicate

    """ This method compares the current node to search_goal. """

    def check_solution(self, current):
        for x in range(len(self.search_goal.val)):
            for y in range(len(self.search_goal.val)):
                if current.val[x][y] != self.search_goal.val[x][y]:
                    return False

        return True

    """"""""""""""""""""""""""""""""""""""" EXPAND NODE METHODS """""""""""""""""""""""""""""""""""""""

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

        # Get and store the index of the "blank" tile in curr_node
        index = self.find_blank(curr_node)
        x = index[0]
        y = index[1]

        # Create list to store the nodes expanded from curr_node
        options = []

        # UP
        if x > 0:
            # Create deep copy of curr_node's state so that original won't be altered
            new_list = copy.deepcopy(curr_node.val)
            # Swap "blank" with whatever "tile" is stored in the row above it on the puzzle
            new_list[x - 1][y], new_list[x][y] = new_list[x][y], new_list[x - 1][y]
            # Create new node, using the new_list puzzle state as its value
            n = Node(new_list, curr_node, curr_node.g + 1)
            # If new node is not a duplicate, add to options list
            if not self.check_duplicate(n):
                options.append(n)
        # DOWN
        if x < 2:
            new_list = copy.deepcopy(curr_node.val)
            new_list[x + 1][y], new_list[x][y] = new_list[x][y], new_list[x + 1][y]
            n = Node(new_list, curr_node, curr_node.g + 1)
            if not self.check_duplicate(n):
                options.append(n)
        # LEFT
        if y > 0:
            new_list = copy.deepcopy(curr_node.val)
            new_list[x][y - 1], new_list[x][y] = new_list[x][y], new_list[x][y - 1]
            n = Node(new_list, curr_node, curr_node.g + 1)
            if not self.check_duplicate(n):
                options.append(n)
        # RIGHT
        if y < 2:
            new_list = copy.deepcopy(curr_node.val)
            new_list[x][y + 1], new_list[x][y] = new_list[x][y], new_list[x][y + 1]
            n = Node(new_list, curr_node, curr_node.g + 1)
            if not self.check_duplicate(n):
                options.append(n)

        return options

    """"""""""""""""""""""""""""""""""""""" BREADTH FIRST SEARCH """""""""""""""""""""""""""""""""""""""

    def breadth_first_search(self):

        current = self.search_start  # Create our 'current' node and set it equal to the puzzle start
        self.open_list.enqueue_bfs(current)  # Enqueue the current node

        # While loop to continue expanding nodes until solution is reached
        while self.check_solution(current) is False:

            current = self.open_list.dequeue()  # dequeue front of PQ

            while self.check_duplicate(current) is True:  # Loop until we find a non-duplicate
                current = self.open_list.dequeue()

            temp_list = self.expand(current)  # temp list to hold our expanded options

            for x in range(len(temp_list)):  # for loop to enqueue all expanded options
                self.open_list.enqueue_bfs(temp_list[x])

            self.closed_list.append(current)  # Add the current node to the end of the closed_list

        self.print_path(current)
        print("Open List Size: ", len(self.open_list.queue))
        print("Closed List Size: ", len(self.closed_list))

    """"""""""""""""""""""""""""""""""""""" MISPLACED TILES """""""""""""""""""""""""""""""""""""""

    """ Compare node n to goal state and return number of tiles "misplaced" """
    def num_misplaced(self, n):

        num_misplaced = 0

        for i in range(3):
            for j in range(3):
                if n.val[i][j] is not self.search_goal.val[i][j]:
                    if n.val[i][j] is not 'X':
                        num_misplaced += 1

        return num_misplaced

    """ This method runs the misplaced tiles puzzle solver. """
    def misplaced_tiles(self):

        # Begin with a node holding the user-input start state
        curr_node = self.search_start
        self.open_list.enqueue(curr_node)

        while not self.check_solution(curr_node):

            # Store the cheapest unexpanded node in curr_node
            curr_node = self.open_list.dequeue()

            # Expand curr_node and store new nodes inside temp
            options = self.expand(curr_node)

            # Update f value (g + number of misplaced tiles) in all options
            # Enqueue updated node into open list
            for i in range(len(options)):
                options[i].f = options[i].g + self.num_misplaced(options[i])
                self.open_list.enqueue(options[i])

            # Add current node to closed list
            self.closed_list.append(curr_node)

        self.print_path(curr_node)
        print("Open List Size: ", len(self.open_list.queue))
        print("Closed List Size: ", len(self.closed_list))

    """"""""""""""""""""""""""""""""""""""" MANHATTAN DISTANCE """""""""""""""""""""""""""""""""""""""

    """ This method returns the index of a given element in a 2D list """
    def get_index(self, n, a):

        index = [0, 0]

        for i in range(3):
            for j in range(3):
                if n.val[i][j] is a:
                    index = [i, j]

        return index

    """ This method returns the total 'manhattan distance' of a puzzle state """
    def distance(self, curr_node):

        # start with a total distance of zero
        dist = 0

        # find and sum distances of tiles 1 - 8 from their current to goal states
        for i in range(9):
            # get the index of the tile in both curr_node and the goal state
            tile_a = self.get_index(curr_node, i)
            tile_b = self.get_index(self.search_goal, i)
            # add the distance of individual tile to total distance
            dist += (abs(tile_a[0] - tile_b[0]) + abs(tile_a[1] - tile_b[1]))

        return dist

    """ This method runs the manhattan distance puzzle solver. """
    def manhattan_distance(self):

        # Begin with a node holding the user-input start state
        curr_node = self.search_start
        self.open_list.enqueue(curr_node)

        while not self.check_solution(curr_node):

            # Store the cheapest unexpanded node in curr_node
            curr_node = self.open_list.dequeue()

            # Expand curr_node and store new nodes inside temp
            options = self.expand(curr_node)

            # Update f value (g + number of misplaced tiles) in all options
            # Enqueue updated node into open list
            for i in range(len(options)):
                options[i].f = options[i].g + self.distance(options[i])
                self.open_list.enqueue(options[i])

            # Add current node to closed list
            self.closed_list.append(curr_node)

        self.print_path(curr_node)
        print("Open List Size: ", len(self.open_list.queue))
        print("Closed List Size: ", len(self.closed_list))

    """""""""""""""""""""""""""""""""""""""      GASCHNIG      """""""""""""""""""""""""""""""""""""""

    """ This method runs the gaschnig puzzle solver. """
    def gaschnig(self):
        print("Welcome to gaschnig. I'm not sure what this is but it sounds cool.")
