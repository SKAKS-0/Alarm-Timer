from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(sec):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < sec:
        time.sleep(1)
        time_elapsed += 1

        remain_time = sec - time_elapsed
        min_remain = remain_time // 60
        sec_remain = remain_time % 60

        print(f"{CLEAR_AND_RETURN}{min_remain:02d}:{sec_remain:02d}")
    playsound("sound.mp3")


mins = int(input("Insert number of minutes: "))
sec = int(input("Insert number of seconds: "))
total_sec = mins * 60 + sec

alarm(total_sec)
