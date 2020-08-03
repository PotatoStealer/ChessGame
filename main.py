from chess import Board, King, Queen, Bishop, Knight, Rook, Pawn
from interface import ConsoleInterface, TextInterface

ui = TextInterface()
game = Board(debug=False, 
            printf=ui.set_msg,
            inputf=ui.get_player_input,
            setboardf=ui.set_board)
game.start()
while game.winner is None:
    game.display()
    start, end = game.prompt()
    game.update(start, end)
    game.next_turn()
print(f'Game over. {game.winner} player wins!')
