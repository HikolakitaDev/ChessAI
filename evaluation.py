import chess

def evaluate_board(board: chess.Board) -> int:
    # Basic logic to evaluate the board position
    # Gotta add : pawn structure evaluation, piece square tables, king safety and soo much more
    piece_values = {
        chess.PAWN: 100,
        chess.KNIGHT: 320,
        chess.BISHOP: 330,
        chess.ROOK: 500,
        chess.QUEEN: 900,
        chess.KING: 20000
    }

    white_material = 0
    for piece_type in piece_values:
        white_material += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]

    black_material = 0
    for piece_type in piece_values:
        black_material += len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]

    return white_material - black_material