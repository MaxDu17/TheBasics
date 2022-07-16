import time
import keyboard
import threading
import queue

CRITICAL_KEYS = list(["space", "left", "right"])
# this is code on how you can read keystrokes from anywhere. All you need is the CRITICAL_KEYS
def read_everything():
    def _check_critical_keys_pressed(input_queue):
        """
        This function will busy-wait until keys are pressed. It registers one event per keypress. It sleeps to prevent excessive CPU usage
        :param input_queue: passed by reference, keeps track of what has been pressed
        :return:
        """
        while True:
            # check if one key is pressed
            while True:
                time.sleep(0.01)  # so we don't take like all the CPU
                done = False
                for key in CRITICAL_KEYS:
                    if keyboard.is_pressed(key):
                        input_queue.put(key)
                        done = True
                        break
                if done:
                    break
            # check if all keys are no longer pressed
            while True:
                time.sleep(0.01)
                done = True
                for key in CRITICAL_KEYS:
                    if keyboard.is_pressed(key):
                        done = False
                if done:
                    break

    input_queue = queue.Queue()
    kb_input_thread = threading.Thread(target=_check_critical_keys_pressed, args=(input_queue,))
    kb_input_thread.daemon = True
    kb_input_thread.start()
    # Main logic loop
    while True:
        if not input_queue.empty():
            button = input_queue.get()
            print(button)
            # do more stuff here
        time.sleep(0.05)  # seconds

# PUT YOUR CURSOR OVER THE TERMINAL, OR A BLANK SPOT ON THIS CODE BEFORE RUNNING
keyboard.press_and_release('shift+s, space') #for specific keys
keyboard.write('The quick brown fox jumps over the lazy dog.') #for general typing
keyboard.wait('esc') #wait until this button. Can only monitor one button at a time

# you can do "keylogging" using this feature, although please be responsible!
# Record events until 'esc' is pressed.
recorded = keyboard.record(until='esc') #it's a list of keyboard event objects
# # Then replay back at three times the speed.
keyboard.play(recorded, speed_factor=3)

keyboard.add_abbreviation('@thebee', 'the bee is a very interesting creature') #this works on notepad and word and other text editors

# # Block forever. You need this if you are doing shortcuts, etc
keyboard.wait()
