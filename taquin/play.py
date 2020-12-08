from game.state import State
from algorithm.a_star import a_star
from algorithm.heuristics import *

import re
import os

# Activating colored output on windows cmd
os.system('COLOR')

start = []
goal = []

pattern = re.compile("^([0-9] ){8}[0-9]$")


def input_state(state_name):
    print("Enter the series of numbers for the " + state_name + " state: ")
    values = input("Distinct values in [0,8] range separated by spaces! : ").strip()
    digits = values.split(" ")

    while not pattern.match(values) or sorted([int(item) for item in digits]) != [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        values = input(
            "Wrong format! Please re enter distinct digits in range 0 to 8 separated with spaces: \n ").strip()
        digits = values.split(" ")

    values_list = [int(item) for item in digits]
    return values_list


initial = State(input_state("initial"))
print("initial state: ")
initial.print_board()

goal = State(input_state("goal"))
print("goal state: ")
goal.print_board()

if not initial.is_solvable(goal):
    print('\33[91m' + "This case is not solvable! \n")
else:
    total_visited = 0
    while True:
        print('Choose heuristic or quit: '
              '\n 1- Sum of manhattan distances '
              '\n 2- Number of falsely placed tiles '
              '\n 3- Quit')
        choice = input("Please enter the number of your choice: ")
        while not choice.isnumeric() or int(choice) not in [1, 2, 3]:
            choice = input("Incorrect option! Please reenter the number of your choice: ")

        if int(choice) == 1:
            total_visited = a_star(initial, goal, heuristic=sum_manhattan_distance)
        elif int(choice) == 2:
            total_visited = a_star(initial, goal, heuristic=falsely_positioned_tiles)
        else:
            exit(0)

        print('\33[92m' + "This case was solved! \n  Total of visited nodes =  " + str(total_visited) + '\33[0m')
