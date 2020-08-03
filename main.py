from chess import Board, King, Queen, Bishop, Knight, Rook, Pawn
from interface import ConsoleInterface

ui = ConsoleInterface()
game = Board(debug=False, 
            printf=ui.set_msg,
            inputf=ui.get_player_input)
game.start()
while game.winner is None:
    game.display()
    start, end = game.prompt()
    game.update(start, end)
    game.next_turn()
print(f'Game over. {game.winner} player wins!')
