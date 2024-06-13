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

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR}{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")  # Use f-string for formatted output
    playsound("5_Alarm_clock/alarm.mp3")

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds

# Call the alarm function with the desired duration in seconds
alarm(total_seconds)