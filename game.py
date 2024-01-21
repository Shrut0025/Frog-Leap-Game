def display_board(positions):
    print("[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]")
    print(positions)


def make_move(positions, frog_position):
    frog_position = int(frog_position)

    if frog_position < 0 or frog_position > 6:
        print("Invalid move. Position should be between 0 and 6.")
        return positions

    if positions[frog_position] == '-':
        print("Invalid move. Empty leaf cannot be moved.")
        return positions

    # Check if the move is valid based on the rules
    if positions[frog_position] == 'G':
        # Green frogs can only move to the right
        if frog_position + 1 <= 6 and positions[frog_position + 1] == '-':
            positions[frog_position], positions[frog_position + 1] = positions[frog_position + 1], positions[frog_position]
        elif frog_position + 2 <= 6 and positions[frog_position + 2] == '-' and positions[frog_position + 1] == 'B':
            positions[frog_position], positions[frog_position + 2] = positions[frog_position + 2], positions[frog_position]
        else:
            print("Invalid move. Check the rules for frog leap.")
    elif positions[frog_position] == 'B':
        # Brown frogs can only move to the left
        if frog_position - 1 >= 0 and positions[frog_position - 1] == '-':
            positions[frog_position], positions[frog_position - 1] = positions[frog_position - 1], positions[frog_position]
        elif frog_position - 2 >= 0 and positions[frog_position - 2] == '-' and positions[frog_position - 1] == 'G':
            positions[frog_position], positions[frog_position - 2] = positions[frog_position - 2], positions[frog_position]
        else:
            print("Invalid move. Check the rules for frog leap.")

    return positions


def is_winner(positions):
    # Check if all brown frogs are on the left, all green frogs are on the right, and the 3rd position is empty
    return positions == ['B', 'B', 'B', '-', 'G', 'G', 'G']


def frog_leap_game():
    positions = ['G', 'G', 'G', '-', 'B', 'B', 'B']

    while True:
        display_board(positions)
        frog_position = input("Enter the position of the frog you want to move (0-6, or 'q' to quit): ")

        if frog_position.lower() == 'q':
            print("Quitting the game.")
            break

        positions = make_move(positions, frog_position)

        if is_winner(positions):
            print("Congratulations! You've won the Frog Leap game🥳")
            break


frog_leap_game()