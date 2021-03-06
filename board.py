from copy import deepcopy
from os import system
from queue import Queue
from random import randint, seed

class Board:
    """Models the board for the game (15 puzzle)"""

    MAX_ROW = 4
    MAX_COL = 4
    SHUFFLE_MAGNITUDE = 20

    def __init__(self):
        """Initialize the board"""

        self.goal = [
            [" 1", " 2", " 3", " 4"], 
            [" 5", " 6", " 7", " 8"], 
            [" 9", "10", "11", "12"], 
            ["13", "14", "15", "__"]
        ]
        self.board = deepcopy(self.goal)
        self.empty_loc = [Board.MAX_ROW - 1, Board.MAX_COL - 1]
        self.moves = {0: self.move_up, 1: self.move_right, 
                        2: self.move_down, 3: self.move_left}
    
    def __repr__(self):
        """Represent the board"""

        for i in range(Board.MAX_ROW):
            for j in range(Board.MAX_COL):
                print(self.board[i][j], end=' ')
            print()
        
        # __repr__ must return some string
        return ""
    
    def refresh(self):
        """Clear the terminal and printing the board"""

        system('clear')
        print('Welcome to the game of fifteen!\n')
        print(self)

        if self.board == self.goal:
            print('Congrats! You Won!')
            return False
        
        return True
    
    def shuffle(self):
        """Randomizes board using succession of legal moves"""

        seed()

        # Shuffle
        for _ in range(Board.SHUFFLE_MAGNITUDE):
            m = randint(0, 3)
            self.moves[m](self.board, self.empty_loc)
        
        # for aesthetic purposes, move empty tiles to the lower right corner
        for _ in range(Board.MAX_ROW):
            self.moves[2](self.board, self.empty_loc)
        
        for _ in range(Board.MAX_COL):
            self.moves[1](self.board, self.empty_loc)


    def move(self, board, e_loc, x, y):
        """Make legal move"""

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
    
    def solve(self):
        """Solves the game using Breadth First Search `BFS` Algorithm"""
        # self.board = deepcopy(self.goal)

        def successors(board, empty_loc):
            """Helper function that extract the children of the current node baord"""
            board_list = [
                deepcopy(board), deepcopy(board),
                deepcopy(board), deepcopy(board)
            ]
            empty_loc_list = [
                list(empty_loc), list(empty_loc),
                list(empty_loc), list(empty_loc)
            ]
            board_list[0], empty_loc_list[0] = (
                self.move_up(board_list[0], empty_loc_list[0])
            )
            board_list[1], empty_loc_list[1] = (
                self.move_right(board_list[1], empty_loc_list[1])
            )
            board_list[2], empty_loc_list[2] = (
                self.move_down(board_list[2], empty_loc_list[2])
            )
            board_list[3], empty_loc_list[3] = (
                self.move_left(board_list[3], empty_loc_list[3])
            )

            return [
                [board_list[0], empty_loc_list[0], 0],
                [board_list[1], empty_loc_list[1], 1],
                [board_list[2], empty_loc_list[2], 2],
                [board_list[3], empty_loc_list[3], 3]
            ]

        # searched = []
        # modify the container of serached node to be set 
        # for optimizing time complexity, since sets in python are 
        # hashable
        searched = set()
        fringe = Queue()
        root = self.board

        fringe.put({'board': root, 'empty_loc': self.empty_loc, 'path': []})

        while True:
            # quit if no solution is found
            if fringe.empty():
                return []
            
            # inspect current node
            node = fringe.get()

            # quit if node have the goal state
            if node['board'] == self.goal:
                return node['path']
            
            # add current node to searched set; put children in fringe
            if str(node['board']) not in searched: # using set instead
                # searched.append(node['board'])
                searched.add(str(node['board'])) # using set instead

                for child in successors(node['board'], node['empty_loc']):
                    if str(child[0]) not in searched:
                        fringe.put({
                            'board': child[0],
                            'empty_loc': child[1],
                            'path': node['path'] + [child[2]]
                        })
                    