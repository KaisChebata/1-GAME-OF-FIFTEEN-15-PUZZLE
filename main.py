from pynput import keyboard

from board import Board

board_game = Board()

def main():
    board_game.shuffle()
    board_game.refresh()

    # collect event until released
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()
    
def on_press(key):
    # print('Hello')
    board_game.refresh()

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    elif key == keyboard.Key.up:
        board_game.board, board_game.empty_loc = (
            board_game.move_up(board_game.board, board_game.empty_loc)
        )
    elif key == keyboard.Key.down:
        board_game.board, board_game.empty_loc = (
            board_game.move_down(board_game.board, board_game.empty_loc)
        )
    elif key == keyboard.Key.right:
        board_game.board, board_game.empty_loc = (
            board_game.move_right(board_game.board, board_game.empty_loc)
        )
    elif key == keyboard.Key.left:
        board_game.board, board_game.empty_loc = (
            board_game.move_left(board_game.board, board_game.empty_loc)
        )
    
    board_game.refresh()
    

if __name__ == '__main__':
    main()