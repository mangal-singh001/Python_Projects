# Python program to convert 
# text to speech 
  
# import the required module from text to speech conversion 
import win32com.client 
  
# Calling the Dispatch method of the module which  
# interact with Microsoft Speech SDK to speak 
# the given input from the keyboard 
  
speaker = win32com.client.Dispatch("SAPI.SpVoice") 

list = ["Rahul","Dev","Mangal","Manish"]
for i in list:
    shoutout = (f"Shoutout to {i}")
    print(shoutout)
    speaker.Speak(shoutout)

  
# To stop the program press 
# CTRL + Z 


import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice") 
while 1: 
    print("Enter the word you want to speak it out by computer") 
    s = input() 
    speaker.Speak(s) 
    break

