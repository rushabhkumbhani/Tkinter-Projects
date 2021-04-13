import pyttsx3 # text to speech conversion library in python
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') # microsoft speech API to use inbuilt voices
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id) #voices[0] is male voice and voices[1] is female voice

def speak(audio): # It wil program jarvis to speak something
    engine.say(audio) # engine will speak audio string
    engine.runAndWait()

def wishMe(): # Make jarvis wish us according to the time
    hour = int(datetime.datetime.now().hour) # we'll get hour from 0 to 24
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis sir. Please tell me how may I help you?")

def takeCommand(): # It will allow jarvis to take microphone input
    # It takes microphone input from the user and returns string output and if there is any error returns none string
    r=sr.Recognizer() # recognizes microphone sound 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.5 # default 0.5 in library but we changed it to 1, which might mean we need to increase the speed of speaking
        audio=r.listen(source) 
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, Language='en-in') #language is english with india so that it recognizes our voice
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('rushabhkumbhani1729@gmail.com','Rushabh1729@')
    server.sendmail("rushabhkumbhani1729@gmail.com",to,content)
    server.close()


if __name__ == "__main__":
    #speak("Rushabh is a good boy")
    wishMe()
    while True:
    #if 1:
        query=takeCommand().lower() #command is converted to lower case to match the query easily
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2) #returns 2 sentences from the wikipedia
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        #elif 'play music' in query:
            #music_dir=" " #path
            #songs = os.listdir(music_dir)
            #print(songs) 
            #os.startfile(os.path.join(music_dir, songs[0])) also try random module for playing songs randomly
        elif 'the time' in query:
            strTime-datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
        elif 'open vscode' in query:
            codePath="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to Rushabh' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="rushabh.kict18@sot.pdpu.ac.in"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my Friend Rushabh, I am not able to send this E-Mail")
