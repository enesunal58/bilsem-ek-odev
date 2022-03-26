import time
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat,end='\r')
        time.sleep(1)
        time_sec -= 1
    print("Ders bitti!")

def countdowns(time_secs):
    while time_secs:
        mins, secs = divmod(time_secs, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat,end='\r')
        time.sleep(1)
        time_secs -= 1
    print("Teneffüs bitti!")

a = input("Ders için geri sayım istiyorsanız D teneffüs için istiyorsanız T tuşuna basınız: ")
if a=="D":
    countdown(2400)
elif a=="T":
    countdowns(300)
else:
    print("HATALI GİRİŞ!")
    
