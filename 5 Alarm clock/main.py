from playsound import playsound
import time

# ascii codes to clear and return cursor to start
CLEAR = "\033[2J" 
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    """
    Plays an alarm sound after a specified number of seconds.
    Also displays the remaining time in minutes and seconds format
    during the countdown.

    Args:
        seconds (int): The number of seconds to wait before playing the alarm.
    """

    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR}{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")  # Use f-string for formatted output

# Call the alarm function with the desired duration in seconds
alarm(2)
playsound("alarm")