# Zoe Harris, Rachel Lewis
# CSCE405 Artificial Intelligence
# Programming Assignment #1

from node import Node
from PriorityQueue import PriorityQueue
import copy


class Search:
    def __init__(self, search=None, start=None, goal=None):
        self.search_type = search  # This string denotes which search method will be used to solve the puzzle
        self.search_start = start  # This list the starting state of the puzzle
        self.search_goal = goal  # This list the solution to the puzzle
        self.closed_list = []  # This is a list that holds the nodes that have been expanded
        self.open_list = PriorityQueue()  # This is a list that holds the nodes that need to be expanded

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

    """This prints the current puzzle state."""
    def print_state(self, n):

        arr = n.val
        for i in range(len(arr)):
            print(arr[i][0], " ", arr[i][1], " ", arr[i][2])

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
            new_list = copy.deepcopy(curr_node.val)
            new_list[x - 1][y], new_list[x][y] = new_list[x][y], new_list[x - 1][y]
            n = Node(new_list, curr_node, curr_node.g + 1)
            self.print_state(n)
            options.append(n)
        # DOWN
        if x < 2:
            new_list = copy.deepcopy(curr_node.val)
            new_list[x + 1][y], new_list[x][y] = new_list[x][y], new_list[x + 1][y]
            n = Node(new_list, curr_node, curr_node.g + 1)
            self.print_state(n)
            options.append(n)
        # LEFT
        if y > 0:
            new_list = copy.deepcopy(curr_node.val)
            new_list[x][y - 1], new_list[x][y] = new_list[x][y], new_list[x][y - 1]
            n = Node(new_list, curr_node, curr_node.g + 1)
            self.print_state(n)
            options.append(n)
        # RIGHT
        if y < 2:
            new_list = copy.deepcopy(curr_node.val)
            new_list[x][y + 1], new_list[x][y] = new_list[x][y], new_list[x][y + 1]
            n = Node(new_list, curr_node, curr_node.g + 1)
            self.print_state(n)
            options.append(n)

        return options

    """ This method checks to see if the current node is located in the closed list. If it is, it is removed from the
    open_list. """
    def check_duplicate(self, n):

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

    """ This method prints the path of the solution. """
    def print_path(self):
        print("We need to see your work!")

    """ This method runs the BFS puzzle solver. """
    def breadth_first_search(self):
        print("Congrats, you've made it to BFS! If only it were a BLT.")
        """Algorithm
            for each vertex v   // While check_solution(current) != True
                do: visited = false  // temp_list = expand(curr_node)
                    pred = -1        
            Q = empty queue; 
            flag[s] = true
            enqueue(Q, s)  // for x in range(len(temp_list), open_list.insert_bfs()
            while Q is not empty  // Loop again
                do v = dequeue(Q)
                    for each w adjacent to v
                        do if flag[w] = false
                            then flag[w] = true
                                pred[w] = v
                                enqueue(Q, w)
        """
        """current = self.search_start
        self.open_list.enqueue(current)
        while (self.check_solution(current)):
            temp_list = self.expand(current)
            for x in range(len(temp_list)):
                self.open_list.append(temp_list[x])
            current = self.open_list.dequeue()"""



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