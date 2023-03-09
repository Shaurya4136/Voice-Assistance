import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from AppOpener import close
from AppOpener import open
import random
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning! Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! Sir")  

    else:
        speak("Good Evening! Sir")

    speak("I am Friday please tell me how may I help you")


def takecommand():
    #it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # seconds of non-speaking audio before a phrase is considered complete
        r.energy_threshold = 500       
        audio = r.listen(source)

    try:
        print("Recognizing...")   
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n") 

    except Exception as e:
        #print(e)
        print("say that again please...")
        return "None"        
    return query

 
if __name__ == "__main__":
   wishMe()
   while True:
      query = takecommand().lower()
    #logic for executing tasks based on query
      if 'wikipedia' in query:
        speak('Searching wikipedia...')
        query = query.replace("wikipedia","")
        result = wikipedia.summary(query,sentences=6)      #return 2 sentences
        print(result)
        speak(result)
      elif 'open youtube' in query:
        webbrowser.open("youtube.com")
      elif 'close youtube' in query:
        close("Microsoft Edge")
      elif 'open google' in query:
        open(webbrowser.open("google.com"))
      elif 'close google' in query:
        close("google.com")

      elif 'open instagram' in query:
        webbrowser.open("instagram.com")
      elif 'close instagram' in query:
        close("instagram.com")
      
      elif 'open flipkart' in query:
        webbrowser.open("flipkart.com")
      elif 'close flipkart' in query:
        close("flipkart.com")
            
      elif 'open amazon' in query:
        webbrowser.open("amazon.com") 
      elif 'close amazon' in query:
        close("Microsoft Edge")
            
      elif 'open spotify' in query:
        webbrowser.open("spotify.com")  
      elif 'close spotify' in query:
        close("spotify.com")
        
      elif 'open whatsapp' in query:
        open("WhatsApp")  
      elif 'close whatsapp' in query:
        close("WhatsApp") 
        
      elif 'open File Explorer' in query:
        open("File Explorer")  
      elif 'close file explorer' in query:
        close("File Explorer")   
        
      elif 'open chrome' in query:
        open("Google Chrome")  
      elif 'close chrome' in query:
        close("Google Chrome")   
        
      elif 'open settings' in query:
        open("settings")  
      elif 'close spotify' in query:
        close("settings")   
        
      elif 'open Visual Studio Code' in query:
        open("Visual Studio Code")  
      elif 'close Visual Studio Code' in query:
        close("Visual Studio Code")   
        
      elif 'open This PC' in query:
        open("This PC")  
      elif 'close This PC' in query:
        close("This PC ")
        
      elif 'open VLC' in query:
        open("VLC")  
      elif 'close VLC' in query:
        close("VLC")
        
      
        
      
         
            
      elif 'play music' in query:
        music_dir = "C:\\Users\\shaur\\OneDrive\\Desktop\\Friday\\music_Friday"
        songs = os.listdir(music_dir)
        l=[1,2,3]
        os.startfile(os.path.join(music_dir,songs[random.choice(l)]))
      elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
    

                
                

            


