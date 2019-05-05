from pynput import mouse
from pynput import keyboard
import numpy as np

from output_manager import generate_timestamp


''''''''''''''''''''' 
'Script dynamic vars'
'''''''''''''''''''''
activation_char = 'i'
timespan = 1  # in secs
sampling_rate = 10  # in Hz
time_compensation = 0.35  # in milliseconds
sampling_period = (1/sampling_rate)*1000  # in milliseconds
data_container = np.zeros((sampling_rate*timespan))

print(
    """
    One sample will be taken each %d milliseconds.
    %d samples will be taken in total.
    """ % (sampling_period, sampling_rate*timespan)
)

def unlock(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        if key.char == activation_char:
            return False
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def start_timestamp_generation(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        print('Running...')
        generate_timestamp(
            timespan, 
            sampling_period, 
            data_container, 
            time_compensation
            )
        return False

def test(x, y, button, pressed):
    print('{0} with {2} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y), button))


if __name__ == "__main__":
    print('Press {} to start'.format(activation_char))
    with keyboard.Listener(on_press=unlock) as listener:
        interrupt_flag = listener.join()
        if interrupt_flag: listener.stop()

    print('Listening to mouse click...\n')
    with mouse.Listener(on_click=start_timestamp_generation) as listener:
        listener.join()
