import matplotlib.pyplot as plt
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import pywhatkit

# Initialize speech engine and microphone
speaker = pyttsx3.init()
mic = sr.Recognizer()

# Welcome message
speaker.say("Welcome")
speaker.runAndWait()

with sr.Microphone() as source:
    print("Start speaking...")
    audio = mic.listen(source)

try:
    text = mic.recognize_google(audio)
    print("You said:", text)

    # Open Notepad
    if "notepad" in text.lower():
        print("Opening Notepad...")
        os.system("Notepad")

    # Open Chrome
    elif "chrome" in text.lower():
        print("Opening Chrome...")
        os.system("Chrome")

    # Send WhatsApp message
    elif "send message" in text.lower():
        print("Sending WhatsApp message...")
        pywhatkit.sendwhatmsg_instantly("+917014492226", "Hi, I'm Lilli")

    else:
        print("Command not recognized")

except Exception as e:
    print("Sorry, I could not understand.")
    print("Error:", e)