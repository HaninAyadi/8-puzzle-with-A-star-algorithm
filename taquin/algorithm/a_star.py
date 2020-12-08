from algorithm.utility import PriorityQueueSet
import matplotlib.pyplot as plt

"""
The a_star function implements the a_star algorithm and returns the total number of visited nodes
"""


def a_star(initial, final, heuristic):
    open_queue = PriorityQueueSet()
    closed_queue = []

    open_queue.add(initial, initial.heuristic_value(heuristic, final))

    while len(open_queue.heap) != 0:

        priority, current_state = open_queue.pop()

        if current_state.heuristic_value(heuristic, final) == 0:
            if len(closed_queue) != 0:
                optimal_path = reconstitute_path(closed_queue[-1], final)
                optimal_path.reverse()
                for state in optimal_path:
                    state.print_board()
                plot_path(closed_queue, optimal_path)

            return len(closed_queue)
        else:
            successors = current_state.generate_next_states()
            for successor in successors:
                h = successor.heuristic_value(heuristic, final)
                g = successor._cost_
                f = g + h
                if not ((successor in closed_queue) or (
                        open_queue.has_item(successor) and (open_queue.get_priority(successor) - h < g))):
                    open_queue.add(successor, f)
            closed_queue.append(current_state)
    return len(closed_queue)


def reconstitute_path(prefinal, final):
    optimal_path = [final]
    current_state = prefinal
    while current_state._parent_ is not None:
        optimal_path.append(current_state)
        current_state = current_state._parent_
    optimal_path.append(current_state)
    return optimal_path


def plot_path(visited, optimal):
    reached_visited = range(0, len(visited))
    reached_optimal = []
    total_optimal_nodes = 0
    for i in reached_visited:
        if optimal[total_optimal_nodes] == visited[i]:
            total_optimal_nodes = total_optimal_nodes + 1
        reached_optimal.append(total_optimal_nodes)

    plt.plot(reached_visited, reached_optimal)
    plt.xlabel("Number of visited nodes")
    plt.ylabel("Number of optimal nodes")
    plt.show()
