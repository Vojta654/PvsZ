import time

def timer():
    start_time = None
    while True:
        if start_time is None:
            start_time = time.time()  # Get the current time in seconds

        elapsed_time = time.time() - start_time  # Calculate the elapsed time
        minutes = int(elapsed_time // 60)  # Calculate the minutes
        seconds = int(elapsed_time % 60)  # Calculate the seconds

        # Format the time display
        timer_display = "{:02d}:{:02d}".format(minutes, seconds)

        # Clear the console (for better display)
        print("\033c", end="")

        # Print the timer display
        print("Timer: {}".format(timer_display))

        time.sleep(1)  # Delay for 1 second

        # Check if the user wants to reset the timer
        if seconds == 5:
            start_time = None  # Reset the start_time to None

timer()


import time
import threading

class Timer:
    def __init__(self):
        self.start_time = None
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True
            threading.Thread(target=self._run_timer).start()

    def stop(self):
        self.is_running = False

    def reset(self):
        self.start_time = None

    def _run_timer(self):
        while self.is_running:
            elapsed_time = time.time() - self.start_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            timer_display = "{:02d}:{:02d}".format(minutes, seconds)
            print("Timer: {}".format(timer_display))
            time.sleep(1)

# Create multiple Timer instances
timer1 = Timer()
timer2 = Timer()

# Start the timers
timer1.start()
timer2.start()

# Simulate timers running for 5 seconds
time.sleep(5)

# Stop timer1 and reset timer2
timer1.stop()
timer2.reset()

# Start timer2 again
timer2.start()

# Simulate timers running for 3 seconds
time.sleep(3)

# Stop both timers
timer1.stop()
timer2.stop()
