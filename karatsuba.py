from utils import *
from search import *

class NQueensProblem(Problem):
    def __init__(self, N):
        self.N = N
        # Generate a random initial state
        initial = sequence(tuple(random.randint(0, N - 1) for _ in range(N)))
        super().__init__(initial, goal=None)

    def actions(self, state):
        # Generate all possible moves for each queen
        actions = []
        for row in range(self.N):
            for col in range(self.N):
                if col != state[row]:  # Ensure the move is to a new column
                    actions.append((row, col))
        return actions  # Each action is unique

    def result(self, state, action):
        # Apply the action to the state
        state = list(state)
        row, col = action
        state[row] = col
        return tuple(state)

    def goal_test(self, state):
        # The goal is achieved when there are no attacking pairs
        return self.value(state) == 0

    def value(self, state):
        # Calculate the number of attacking pairs
        attacking_pairs = 0
        for row1 in range(self.N):
            for row2 in range(row1 + 1, self.N):
                col1 = state[row1]
                col2 = state[row2]
                if col1 == col2 or abs(col1 - col2) == abs(row1 - row2):
                    attacking_pairs += 1
        return attacking_pairs

def print_board(state):
    N = len(state)
    for row in range(N):
        line = ""
        for col in range(N):
            if state[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

def hill_climbing(problem):
    current = Node(problem.initial)
    print("Initial state:")
    print_board(current.state)  # Print the initial board configuration
    print(f"Number of attacking pairs: {problem.value(current.state)}")  # Display the number of attacking pairs
    moves = 0  # Initialize move counter

    while True:
        neighbors = current.expand(problem)
        if not neighbors:
            break

        neighbor = argmin_random_tie(neighbors, key=lambda node: problem.value(node.state))
        if problem.value(neighbor.state) >= problem.value(current.state):
            break

        current = neighbor
        moves += 1  # Increment move counter for each state transition
        print("Moved to state (Move {}):".format(moves))
        print_board(current.state)  # Print the new board configuration after each move
        print(f"Number of attacking pairs: {problem.value(current.state)}")  # Display the number of attacking pairs

    print("Final state after {} moves:".format(moves))
    print_board(current.state)  # Print the final board configuration
    print(f"Number of attacking pairs: {problem.value(current.state)}")  # Display the number of attacking pairs
    return current.state  # Return only the final state





def random_restart_hill_climbing(problem, num_restarts=100):
    for _ in range(num_restarts):
        # Generate a new random initial state
        problem.initial = tuple(random.randint(0, problem.N - 1) for _ in range(problem.N))
        solution = hill_climbing(problem)
        value = problem.value(solution)

        # If a solution with 0 attacking pairs is found, return immediately
        if value == 0:
            print("Solution found:")
            print_board(solution)
            print(f"Number of attacking pairs: {value}")
            return solution

    # If no solution is found after all restarts, indicate failure
    print("No solution found after {} restarts.".format(num_restarts))
    return None


def main(N):
    problem = NQueensProblem(N)
    solution = random_restart_hill_climbing(problem)
    print(f"Final board configuration: {solution}")
    print(f"Number of attacking pairs: {problem.value(solution)}")

if __name__ == "__main__":
    N = int(input("Enter the value of N for the N-Queens problem: "))
    main(N)
