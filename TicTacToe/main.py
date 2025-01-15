from TicTacToe.Board import Board
from TicTacToe.Game import Game
from TicTacToe.Player import Player

alex = Player("Smart Alex", "X")
bob = Player("Big Bob", "O")
board = Board(3)
game = Game(alex, bob, board)

game.play_game()