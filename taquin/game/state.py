import numpy as np

class State:
    """ Class that describes a state of the 8 puzzle"""

    def __init__(self, values, parent=None):
        """ A state is described by the ordered list of its values, the possible actions on that state"""

        self._values_ = values
        self._actions_ = self.get_possible_actions()
        self._parent_ = parent
        if parent is None:
            self._cost_ = 0
        else:
            self._cost_ = self._parent_._cost_ + 1

    def __eq__(self, other):
        """ Two states are equal if their lists of values are equal"""

        return self._values_ == other._values_

    def __hash__(self):
        """ overriding __eq__ implies redefining __hash__"""

        return id(self._values_)

    def get_possible_actions(self):
        """ Identifying the possible actions in a dictionary where the movable tile is assigned to a sliding action """

        pos_empty = self._values_.index(0)
        possible_actions = {}
        if pos_empty not in [0, 3, 6]:
            possible_actions[pos_empty - 1] = "R"
        if pos_empty not in [2, 5, 8]:
            possible_actions[pos_empty + 1] = "L"
        if pos_empty not in [6, 7, 8]:
            possible_actions[pos_empty + 3] = "U"
        if pos_empty not in [0, 1, 2]:
            possible_actions[pos_empty - 3] = "D"
        return possible_actions

    def generate_next_states(self):
        """ Generating the next states that are possible from the current state based on the possible action """

        pos_empty = self._values_.index(0)
        successors = []
        for key in self._actions_:
            """initializing the values for the child state"""
            values = self._values_.copy()

            """permutation between the movable tile and the empty position"""
            values[pos_empty] = values[key] + values[pos_empty]
            values[key] = values[pos_empty] - values[key]
            values[pos_empty] = values[pos_empty] - values[key]

            """appending the child state to the list of successors"""
            successors.append(State(values, self))
        return successors

    def print_board(self):
        """ Printing the current state in a grid layout """

        board = np.reshape(self._values_, (3, 3))
        for i in range(3):
            print("------------")
            for j in range(3):
                if board[i][j] == 0:
                    print('\33[6m' + '\33[97m' + '\33[47m' + "| " + str(board[i][j]) + " " + '\33[0m', end='')
                else:
                    print('\33[97m' + '\33[44m' "| " + str(board[i][j]) + " " + '\33[0m', end='')
            print("")
        print("------------")

    def heuristic_value(self, heuristic, goal):
        """ Estimating the distance between the current state and the goal based on a given heuristic function """

        return heuristic(self, goal)

    def is_solvable(self, goal):
        """ Test to see if going from the current state to the goal is possible based on the parity of inversions """

        start_values = self._values_.copy()
        goal_values = goal._values_.copy()

        start_values.remove(0)
        goal_values.remove(0)

        def index_mapper_function(element):
            return goal_values.index(element)

        mapped_values = list(map(index_mapper_function, start_values))
        inversions_count = 0
        for i in range(8):
            for j in range(i + 1, 8):
                if mapped_values[i] > mapped_values[j]:
                    inversions_count += 1

        return inversions_count % 2 == 0
