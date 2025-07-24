import chess
from evaluation import evaluate_board

def find_best_move(board: chess.Board, depth: int):

    best_move = None

    is_maximizing_player = (board.turn == chess.WHITE)

    if is_maximizing_player:
        best_value = -float('inf')
    else:
        best_value = float('inf')

    for move in board.legal_moves:
        board.push(move)

        board_value = minimax(board, depth - 1, -float('inf'), float('inf'), not is_maximizing_player)

        board.pop()

        if is_maximizing_player:
            if board_value > best_value:
                best_value = board_value
                best_move = move
        else:
            if board_value < best_value:
                best_value = board_value
                best_move = move

    print(f"Engine evaluation: {best_value / 100:.2f} pawns")
    return best_move

def minimax(board: chess.Board, depth: int, alpha: float, beta: float, maximizing_player: bool):
    if depth == 0 or board.is_game_over():
        return quiescence_search(board, alpha, beta)

    if maximizing_player:
        max_eval = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval

    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
    
def quiescence_search(board: chess.Board, alpha: float, beta: float) -> int:
    stand_pat = evaluate_board(board)
    
    if stand_pat >= beta:
        return beta
    if alpha < stand_pat:
        alpha = stand_pat

    for move in board.generate_legal_captures():
        board.push(move)
        score = -quiescence_search(board, -beta, -alpha)
        board.pop()
        
        if score >= beta:
            return beta
        if score > alpha:
            alpha = score

    return alpha