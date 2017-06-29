from isolation import Board
from sample_players import *
from game_agent import *

# create an isolation board (by default 7x7)
player1 = RandomPlayer()
# player2 = MinimaxPlayer(score_fn=custom_score)
player2 = AlphaBetaPlayer(score_fn=custom_score)

game = Board(player1, player2)


# place player 1 on the board at row 2, column 3, then place player 2 on
# the board at row 0, column 5; display the resulting board state.  Note
# that the .apply_move() method changes the calling object in-place.
# print('Active player is {}'.format(game.active_player))
game.apply_move((0, 5))

# print('Active player is {}'.format(game.active_player))
game.apply_move((3, 3))

print(game.to_string())

# print('Player 2: {}'.format(game.get_player_location(player2)))

print('Active player is {}'.format(game.active_player))
print('Position: {}'.format(game.get_player_location(game.active_player)))
print('with legal moves: {}'.format(game.get_legal_moves()))

print('Inactive player is {}'.format(game.inactive_player))
print('Position: {}'.format(game.get_player_location(game.inactive_player)))
print('with legal moves: {}'.format(game.get_legal_moves(game.inactive_player)))

winner, history, outcome = game.play()
print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
print(game.to_string())
print("Move history: {} moves.\n{!s}".format(len(history), history))

