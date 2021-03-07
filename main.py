from pynput import keyboard

from board import Board

board = Board()

def main():
    print(board)

    # collect event until released
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()
    
def on_press(key):
    print('Hello')

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
    

if __name__ == '__main__':
    main()