import chess
from search import find_best_move

board = chess.Board()

def print_board():
    print(board)

def make_move(move):
    board.push(chess.Move.from_uci(move))

def is_legal_move(move):
    return chess.Move.from_uci(move) in board.legal_moves

def turn():
    return board.turn

def get_game_phase(board: chess.Board):

    phase_values = { chess.KNIGHT: 1, chess.BISHOP: 1, chess.ROOK: 2, chess.QUEEN: 4 }
    phase = 0
    for piece_type in phase_values:
        phase += len(board.pieces(piece_type, chess.WHITE)) * phase_values[piece_type]
        phase += len(board.pieces(piece_type, chess.BLACK)) * phase_values[piece_type]
    return phase


if __name__ == "__main__":

    while True:
        if board.is_checkmate():
            print("\n--- CHECKMATE! ---")
            print("Result: " + board.result())
            print_board()
            break
        if board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves() or board.is_fivefold_repetition():
            print("\n--- DRAW! ---")
            print("Result: " + board.result())
            print_board()
            break

        print_board()

        if turn() == chess.WHITE:
            move_uci = input("\nEnter your move (e.g., e2e4): ")
            try:
                if is_legal_move(move_uci):
                    make_move(move_uci)
                else:
                    print("\n### ILLEGAL MOVE! Try again. ###")
            except ValueError:
                print(f"\n### INVALID MOVE FORMAT: '{move_uci}'. Use UCI notation (e.g., e2e4). ###")

        else:
            print("\nBot is thinking...")
            phase = get_game_phase(board)

            if phase > 18:  # opening
                search_depth = 3
                print(f"(Phase: Opening, Depth: {search_depth})")
            elif phase > 6:  # midgame
                search_depth = 3
                print(f"(Phase: Middlegame, Depth: {search_depth})")
            else:  # endgame
                search_depth = 5
                print(f"(Phase: Endgame, Depth: {search_depth})")
            bot_move = find_best_move(board, search_depth)

            if bot_move is not None:
                print(f"Bot plays: {bot_move.uci()}")
                make_move(bot_move.uci())
            else:
                print("Bot has no legal moves. This might be a bug or the game ended.")
                break