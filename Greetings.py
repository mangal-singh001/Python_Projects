import time
import win32com.client
speaker = win32com.client.Dispatch("SAPI.Spvoice")
clock = time.strftime("%H:%M:%S")
print("Current Time",clock)
timestamp = int(time.strftime("%H"))

if 5 <= timestamp < 12:
    Greeting = "Good morning Dev Verma"
elif 12 <= timestamp < 17:
    Greeting = "Good afternoon Dev Verma"
elif 17 <= timestamp < 21:
    Greeting = "Good evening Dev Verma"
else:
    Greeting = "Good night dev"
print(Greeting)
speaker.speak(Greeting)