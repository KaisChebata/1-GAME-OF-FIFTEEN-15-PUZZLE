# module for testing pynput library
from pynput import mouse
from pynput.mouse import Button, Controller

# Mouse Controlling
mus = Controller()

print('Testing mouse controlling and listening:')
print('-' * 40)
# read pointer position
print(f'The current pointer position is: {mus.position}')

# set pointer position
mus.position = (10, 20)
print(f'pointer moved to position: {mus.position}')

# move pointer relative to current position
mus.move(5, -5)
print(f'pointer position after move: {mus.position}')

# Press and Release
mus.press(Button.left)
mus.release(Button.left)

# Double click: this is different from press and release
# mus.click(Button.left, 2)

# scroll two steps down
mus.scroll(0, 100)

# Mouse Monitoring

def on_move(x, y):
    print(f'Pointer moved to: {(x, y)}')

def on_click(x, y, button, pressed):
    print(f'{"Pressed" if pressed else "Released"} at {(x, y)}')

    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print(f'Scrolled {"down" if dy < 0 else "up"} at {(x, y)}')

# collect events until released
# with mouse.Listener(
#     on_move=on_move,
#     on_click=on_click,
#     on_scroll=on_scroll) as listener:
#     listener.join()

# ... or, in a non-blocking fashoin
# listener = mouse.Listener(
#     on_move=on_move,
#     on_click=on_click,
#     on_scroll=on_scroll
# )
# listener.start()

print()
print('-' * 98)