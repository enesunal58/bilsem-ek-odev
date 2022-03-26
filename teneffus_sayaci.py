import time
def tenefus(time_secs):
    while time_secs:
        mins, secs = divmod(time_secs, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat,end='\r')
        time.sleep(1)
        time_secs -= 1
    print("Teneffüs bitti!")