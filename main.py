import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import pyjokes
import random

print("stating......")
NAME="sir" #change it to your prefered NAME
songs_dir="<file>" #add your music file directory here
ainame="windows"
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id) #choosing male or female voice
def speak(text): #speaks the sent text
  engine.say(text)
  engine.runAndWait()

def wishMe(): #this code wishes the user and the global variable is set as NAME
  hour=int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
    speak("Good morning.. "+NAME)
  elif hour>=12 and hour<6:
    speak("Good afternoon.. "+NAME)
  else:
    speak("Good evening "+NAME)

  #speak("I am your personal assistant how may I help you")

#this function take the voice and convert into command from the microphone
def takeCommand():
  r=sr.Recognizer()
  with sr.Microphone() as source:
    print("listening")
    audio = r.listen(source)
    try:
      print("Recognising")
      query=r.recognize_google(audio,language='en-in')
      print(f"user said: {query}\n")
    except Exception as e:
      print("could not understand..")
      query="hello"
    return query

# Main program starts here
speak("starting....")
wishMe()
def main():
    query=takeCommand()
    comm=query.lower()
    if ainame in comm:
        command=comm.replace(ainame,"")
        if "wikipedia" in command:#searching in wikipedia
          speak("searching..")
          command=command.replace("wikipedia","")
          print(command)
          results=wikipedia.wikipedia.summary(command,sentences=2)
          speak(results)
          page=wikipedia.wikipedia.page(results)
          url=page.url
          speak("To know more check "+url)
          print(url)

        elif "open youtube" in command:# to open youtube
            speak("opening youtube")
            webbrowser.open("https://youtube.com")
        elif "open gmail" in command:# to open gmail
            speak("opening gmail")
            url = "https://mail.google.com/"
            webbrowser.open(url)
        elif "open protonmail" in command:# to open protonmail
            speak("opening proton mail")
            url = "https://protonmail.com/"
            webbrowser.open(url)
        elif "open whatsapp" in command:# to open whatsapp
            speak("opening whatsapp web in browser")
            url = "https://web.whatsapp.com/"
            webbrowser.open(url)
        elif "open project" in command:# to open project on github
            speak("opening namanskshetty in github")
            url = "https://github.com/namanskshetty"
            webbrowser.open(url)
        elif "play on youtube" in command: # to play music on youtube
            song=command.replace("play on youtube","")
            speak("playing"+song)
            pywhatkit.playonyt(song)
        elif 'time' in command:# to tell the time
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)
        elif 'joke' in command:# search for pyjokes
            speak(pyjokes.get_joke())
        elif "play music" in command:# plays music on default music player
            if songs_dir=="<file>":
                speak("please specify your music dir in the code")
            else:
                speak("playing music on default music player")
                songs=os.listdir(songs_dir)
                print(len(songs))
                ma=int(len(songs))#suffles the music
                i=random.randint(0,ma)
                os.startfile(os.path.join(songs_dir,songs[i]))
        elif "exit" in command:
            speak("bye.....")
            return 0

while True:
    a=main()
    if a==0:
        break
