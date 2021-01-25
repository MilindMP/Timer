import time


def speak(str):
    from win32com.client import Dispatch
    speaks = Dispatch("SAPI.SpVoice")
    speaks.Speak(str)


def countdown(t):
    from win32com.client import Dispatch
    speaks = Dispatch("SAPI.SpVoice")
    speaks.Speak(str)
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Time Out!!!")


if __name__ == '__main__':
    speak("Enter the time in second:")
    t = int(input("Enter the time in second:"))

    countdown(t)
speak("Time Out")
