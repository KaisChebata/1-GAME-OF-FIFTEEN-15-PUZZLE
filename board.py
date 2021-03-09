from copy import deepcopy
from os import system

class Board:
    """Models the board for the game (15 puzzle)"""

    MAX_ROW = 4
    MAX_COL = 4

    def __init__(self):
        self.goal = [
            [" 1", " 2", " 3", " 4"], 
            [" 5", " 6", " 7", " 8"], 
            [" 9", "10", "11", "12"], 
            ["13", "14", "15", "__"]
        ]
        self.board = deepcopy(self.goal)
        self.empty_loc = [Board.MAX_ROW - 1, Board.MAX_COL - 1]
    
    def __repr__(self):
        for i in range(Board.MAX_ROW):
            for j in range(Board.MAX_COL):
                print(self.board[i][j], end=' ')
            print()
        
        # __repr__ must return some string
        return ""
    
    def refresh(self):
        """method that clear the terminal and printing the board"""
        system('clear')
        print('Welcome to the game of fifteen!\n')
        print(self)
    
    def move(self, board, e_loc, x, y):
        """General move function, that will moves empty tile around, 
        exchange its position with neighbor tile"""

        # check legality of move
        if (
            e_loc[0] + x < 0 or e_loc[0] + x > 3 or 
            e_loc[1] + y < 0 or e_loc[1] + y > 3
            ):
            return board, e_loc
        
        # swaping empty tile with its neighbor, up, down, right, or left
        # in x, y = y, x fashoin
        # Swap
        board[e_loc[0]][e_loc[1]], board[e_loc[0] + x][e_loc[1] + y] = (
            board[e_loc[0] + x][e_loc[1] + y], board[e_loc[0]][e_loc[1]]
        )

        # update empty tile location
        e_loc[0] += x
        e_loc[1] += y

        return board, e_loc
    
    def move_up(self, board, e_loc):
        """move_up method makes an empty tile moves up"""
        return self.move(board, e_loc, -1, 0)
    
    def move_down(self, board, e_loc):
        """move_down method makes an empty tile moves down"""
        return self.move(board, e_loc, 1, 0)
    
    def move_right(self, board, e_loc):
        """move_right method makes an empty tile moves right"""
        return self.move(board, e_loc, 0, 1)
    
    def move_left(self, board, e_loc):
        """move_left method makes an empty tile moves left"""
        return self.move(board, e_loc, 0, -1)