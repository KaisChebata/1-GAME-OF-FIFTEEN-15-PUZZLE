from pynput import keyboard

from board import Board

board_game = Board()

def main():
    print(board_game)

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
        print('up')
    elif key == keyboard.Key.down:
        print('down')
    elif key == keyboard.Key.left:
        print('left')
    elif key == keyboard.Key.right:
        print('right')
    
    board_game.refresh()
    

if __name__ == '__main__':
    main()