import datetime
import os
from unittest import result
import requests
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour > 1 and hour < 12:
        speak("Good Morning!, Sir")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon!, Sir")
    else:
        speak("I am sleeping")
    
    speak("I am Jarvis Sir How may i help you")

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)
   
def takeCommand():
    #  it take microphone input from the user and return back as a string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        print(f"User said:  {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please ...")
        return "None"
    return query

if __name__ == "__main__":
    # speak("Abhijeet is awesome")
    wishMe()
    while True:
       query = takeCommand().lower()

       if 'wikipedia' in query:
           speak("Searching wikipedia")
           query = query.replace('wikipedia', "")
           results = wikipedia.summary(query, sentences=2)
           print(results)
           speak(results)

       elif 'quit' in query:
           quit()
    
       elif 'open google' in query:
           speak("openning google")
           print("openning google....")
           webbrowser.open('google.com') 

       elif 'open youtube' in query:
           speak("openning youtube")
           print("openning youtube")
           webbrowser.open('youtube.com')
       elif 'who are you' in query:
           speak("I am jarvis and i am your Assitant Sir!") 
           
       elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           print(strTime)
           speak(strTime)
       elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            print(joke)
       elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = takeCommand().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")
       elif "play a happy birthday song" in query:
           webbrowser.open('https://youtu.be/z3grFwJwrD0')
       elif "play woshang clan " in query:
           webbrowser.open("https://www.youtube.com/watch?v=VIE-NMeYAoU") 
       elif "tu chutiya hai" in query:
           speak("Tu   chootiyaa! hai madarchhhhooood!")   
           
        
    
        
        
      
        


        
       
