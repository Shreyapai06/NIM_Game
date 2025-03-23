import sys
import math

def get_first_player():
    while True:
        choice = input("Who plays first? (human/computer): ").strip().lower()
        if choice in ("human", "computer"):
            return choice
        print("Invalid choice. Please enter 'human' or 'computer'.")

def is_terminal(red, blue):
    return red == 0 or blue == 0

def evaluate(red, blue, version):
    score = 2 * red + 3 * blue
    return -score if version == "standard" else score

def get_possible_moves(red, blue):
    moves = []
    for count in [2, 1]:  # Prioritize removing 2 if possible
        if red >= count:
            moves.append(("red", count))
        if blue >= count:
            moves.append(("blue", count))
    return moves

def apply_move(red, blue, move):
    pile, count = move
    return (red - count, blue) if pile == "red" else (red, blue - count)

def minimax(red, blue, depth, alpha, beta, maximizing_player, version, depth_limit=None):
    if is_terminal(red, blue) or (depth_limit is not None and depth >= depth_limit):
        return evaluate(red, blue, version), None

    best_move = None
    if maximizing_player:
        max_eval = -math.inf
        for move in get_possible_moves(red, blue):
            new_red, new_blue = apply_move(red, blue, move)
            eval, _ = minimax(new_red, new_blue, depth + 1, alpha, beta, False, version, depth_limit)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for move in get_possible_moves(red, blue):
            new_red, new_blue = apply_move(red, blue, move)
            eval, _ = minimax(new_red, new_blue, depth + 1, alpha, beta, True, version, depth_limit)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def get_human_move(red, blue):
    while True:
        move = input("Your move (format: red/blue 1/2): ").strip().lower().split()
        if len(move) != 2:
            print("Invalid format. Use: red/blue 1/2")
            continue
        pile, count = move[0], int(move[1])
        if pile not in ("red", "blue") or count not in (1, 2):
            print("Invalid move. Try again.")
            continue
        if (pile == "red" and red < count) or (pile == "blue" and blue < count):
            print(f"Not enough {pile} marbles.")
            continue
        return (pile, count)

def print_state(red, blue):
    print(f"Current state: {red} red, {blue} blue")

def play_game():
    num_red = int(input("Enter number of red marbles: "))
    num_blue = int(input("Enter number of blue marbles: "))
    version = input("Enter game version (standard/misere): ").strip().lower()
    first_player = get_first_player()
    depth_limit = 4  # Set to None for full search
    
    red, blue = num_red, num_blue
    turn = first_player
    
    while not is_terminal(red, blue):
        print_state(red, blue)
        if turn == "computer":
            print("Computer's turn:")
            _, best_move = minimax(red, blue, 0, -math.inf, math.inf, True, version, depth_limit)
            if best_move:
                print(f"Computer removes {best_move[1]} {best_move[0]} marble(s)")
                red, blue = apply_move(red, blue, best_move)
            turn = "human"
        else:
            move = get_human_move(red, blue)
            red, blue = apply_move(red, blue, move)
            turn = "computer"
    
    print_state(red, blue)
    print(f"Game over. {turn} loses.")
    winner = "human" if turn == "computer" else "computer"
    print(f"{winner} wins!")

if __name__ == "__main__":
    play_game()
