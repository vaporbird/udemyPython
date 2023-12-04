#This is a fun NEVER-EXIT program that ignores exceptions (ctrl+c, ctrl + \)

import signal
import time

# Define a signal handler function
def signal_handler(signum, frame):
    print(f" Received signal {signum}. Ignoring. ")

# Set the signal handlers
signal.signal(signal.SIGQUIT, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

# Your main program
try:
    while True:
        print(" Running... ")
        time.sleep(1)
except KeyboardInterrupt:
    print(" Caught KeyboardInterrupt. Exiting. ")
except Exception as e:
    print(f" An error occurred: {e}")
finally:
    # Restore the default signal handlers
    signal.signal(signal.SIGQUIT, signal.SIG_DFL)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
