import math
import numpy as np

# Class containing the methods to solve the maze
class MazeSolver:
    def __init__(self, board):
        #Initialize the MazeSolver with the given board
        self.board = board
        self.goal = (0, 0)

        #Find the initial and goal positions on the board
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x].lower() == "o":
                    self.initial = (x, y)
                elif self.board[y][x].lower() == "x":
                    self.goal = (x, y)

    def actions(self, state):
        #Generate valid actions based on the current state
        actions = []
        for action in COSTS.keys():
            newx, newy = self.result(state, action)
            if self.is_valid(newx, newy):
                actions.append(action)

        return actions

    def result(self, state, action):
        #Calculate the new state based on the action
        x, y = state
        if "up" in action:
            y -= 1
        if "down" in action:
            y += 1
        if "left" in action:
            x -= 1
        if "right" in action:
            x += 1

        new_state = (x, y)
        return new_state

    def is_goal(self, state):
        #Check if the current state is the goal
        return state == self.goal

    def cost(self, state, action, state2):
        #Return the cost of taking a particular action
        return COSTS[action]

    def heuristic(self, state):
        #Calculate the heuristic value based on Euclidean distance
        x, y = state
        gx, gy = self.goal
        return math.sqrt((x - gx) ** 2 + (y - gy) ** 2)

    def is_valid(self, x, y):
        #Check if the new state is within the maze boundaries and not a wall
        return 0 <= x < len(self.board[0]) and 0 <= y < len(self.board) and self.board[y][x] != "#"

    def astar(self):
        #A* algorithm implementation to find the optimal path
        open_set = set()
        closed_set = set()
        start = self.initial
        open_set.add(start)

        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start)}

        while open_set:
            current = min(open_set, key=lambda x: f_score[x])

            if self.is_goal(current):
                #Reconstruct and return the optimal path
                path = self.reconstruct_path(came_from, current)
                return path

            open_set.remove(current)
            closed_set.add(current)

            for action in self.actions(current):
                neighbor = self.result(current, action)
                if neighbor in closed_set:
                    continue

                tentative_g_score = g_score[current] + self.cost(current, action, neighbor)

                if neighbor not in open_set or tentative_g_score < g_score[neighbor]:
                    #Update information for the neighbor
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor)

                    if neighbor not in open_set:
                        open_set.add(neighbor)

        return None

    def reconstruct_path(self, came_from, current):
        #Reconstruct the path by backtracking
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        return total_path[::-1]

#Main entry point when the script is executed
if __name__ == "__main__":
    #Define the maze as a string with walls ('#'), start position ('o'), and goal position ('x')
    MAP = """
    ##############################
    #         #              #   #
    ######    ########       #   #
    #    #   #               #   #
    #    #####   ###    ######   #
    # o    #   ###   #           #
    #      #     #   #  #  #   ###
    #     #####    #    #  #  x  #
    #              #       #     #
    ##############################
    """

    #Print the original maze
    print(MAP)

    #Convert the map string to a list for processing
    MAP = [list(x) for x in MAP.split("\n") if x]

    #Define the costs for different movements in the maze
    cost_regular = 1.0
    cost_diagonal = 1.7

    COSTS = {
        "up": cost_regular,
        "down": cost_regular,
        "left": cost_regular,
        "right": cost_regular,
        "up left": cost_diagonal,
        "up right": cost_diagonal,
        "down left": cost_diagonal,
        "down right": cost_diagonal,
    }

    #Create the maze solver object using the defined map
    solver = MazeSolver(MAP)

    #Run the A* algorithm to find the optimal path
    path = solver.astar()
