from copy import deepcopy

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