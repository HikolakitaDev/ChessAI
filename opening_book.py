import chess
import chess.pgn
import random
import os
from typing import Union

class OpeningBook:
    def __init__(self, pgn_file_path: str):
        self.book = {}
        if not os.path.exists(pgn_file_path):
            print(f"PGN file not found at '{pgn_file_path}'. The opening book will be empty.")
            return
            
        print("Building opening book from PGN...")
        self.build_book(pgn_file_path)
        print(f"Book built successfully with {len(self.book)} unique positions.")

    def build_book(self, pgn_file_path: str):
        with open(pgn_file_path) as pgn:
            while True:
                game = chess.pgn.read_game(pgn)
                if game is None:
                    break  

                board = game.board()
                move_limit = 20 

                for i, move in enumerate(game.mainline_moves()):
                    if i >= move_limit:
                        break

                    position_key = board.board_fen()

                    if position_key not in self.book:
                        self.book[position_key] = []
                    
                    self.book[position_key].append(move.uci())
                    board.push(move)

    def get_move(self, board: chess.Board) -> Union[str, None]:
        position_key = board.board_fen()
        
        if position_key in self.book:
            possible_moves_uci = self.book[position_key]
            legal_moves_uci = {move.uci() for move in board.legal_moves}
            book_legal_moves = [move for move in possible_moves_uci if move in legal_moves_uci]

            if book_legal_moves:
                return random.choice(book_legal_moves)
        
        return None
    

