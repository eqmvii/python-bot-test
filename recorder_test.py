from pynput import mouse
from pynput import keyboard
import logging

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

print("leggo")

# def on_move(x, y):
  # print("alalal i movin")
  # logging.info("Mouse moved to ({0}, {1})".format(x, y))


# don't uncomment this it's totally blocking
def on_click(x, y, button, pressed):
  if pressed:
      logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
  logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

# with Listener(on_click=on_click, on_scroll=on_scroll) as listener:
#   listener.join()

listener = mouse.Listener(on_click=on_click, on_scroll=on_scroll)

listener.start()

def on_release(key):
  print('{0} released'.format(key))
  if key == keyboard.Key.esc:
    # Stop listener
    return False

def on_press(key):
  if key.char == 'q':
    sys.exit()
  try:
    print('alphanumeric key {0} pressed'.format(key.char))
  except AttributeError:
    print('special key {0} pressed'.format(key))

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()

# ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()
