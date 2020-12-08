"""This heuristic function calculates the number of falsely placed tiles compared to the goal"""


def falsely_positioned_tiles(initial_state, final_state):
    sum_false_positions = 0
    for i in range(9):
        if initial_state._values_[i] != 0 and initial_state._values_[i] != final_state._values_[i]:
            sum_false_positions = sum_false_positions + 1
    return sum_false_positions


"""This heuristic function is based on calculating the sum of manhattan distances
   between the initial and final position of each tile"""


def sum_manhattan_distance(initial_state, final_state):
    i_values = initial_state._values_
    f_values = final_state._values_
    s = 0
    for k in range(1, 9):
        xi = i_values.index(k) // 3
        yi = i_values.index(k) % 3
        xf = f_values.index(k) // 3
        yf = f_values.index(k) % 3
        s = s + abs(xi - xf) + abs(yi - yf)
    return s
