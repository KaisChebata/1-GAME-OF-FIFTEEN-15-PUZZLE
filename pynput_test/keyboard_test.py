from pynput.keyboard import Key, Controller
from pynput import keyboard

# Keyboard Controlling
key_board = Controller()

# Press and Release space
key_board.press(Key.space)
key_board.release(Key.space)

# Type a lower case A; this will work even if no key on the
# physical keyboard is labelled 'A'
key_board.press('a')
key_board.release('a')

# Type two upper case As
key_board.press('A')
key_board.release('A')
with key_board.pressed(Key.shift):
    key_board.press('a')
    key_board.release('a')

# Type 'Hello World!' using shortcut type method
key_board.type('Hello World!')

# Monitoring the keyboard

def on_press(key):
    try:
        print(f'alphanumeric key {key.char} pressed')
    except AttributeError:
        print(f'special key {key} pressed')

def on_release(key):
    print(f'{key} released')

    if key == keyboard.Key.esc:
        # Stop Listener
        return False

# collect events until released
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashoin:
# listener = keyboard.Listener(on_press=on_press, on_release=on_release)
# listener.start()

# Handling keyboard listener errors
# class MyException(Exception): pass

# def on_press(key):
#     if key == keyboard.Key.esc:
#         raise MyException(key)

# # collect events untill released
# with keyboard.Listener(on_press=on_press) as listener:
#     try:
#         listener.join()
#     except MyException as e:
#         print(f'{e.args[0]} was pressed')

# Synchronous event listening for the keyboard listener
# read a single event
with keyboard.Events() as events:
    # Block at most one second
    event = events.get(1.0)
    if event is None:
        print('You did not press a key within one second')
    else:
        print(f'Received event {event}')

# iterate over keyboard events
# The event listener will be running in this block
with keyboard.Events() as events:
    for event in events:
        if event.key == Key.esc:
            break
        else:
            print(f'Received event {event}')
