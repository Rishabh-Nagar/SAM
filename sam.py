import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

print(voices[0].id)

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    
    elif hour >=12 and hour < 18:
        speak("Good afternoon sir!")

    else:
        speak("Good evening sir!")

    speak("I am SAM. How may i assiste you sir")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said :{query}\n")

    except Exception() as e:
        #print(e)

        print("say that again")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email.id', '*password*')
    server.sendmail('email.id', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
        
        elif "open google" in query:
            webbrowser.open("https://www.google.com")

        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com")

        elif "open insta inbox" in query:
            webbrowser.open("https://www.instagram.com/direct/inbox/")

        elif "open geeksforgeeks" in query:
            webbrowser.open("https://www.geeksforgeeks.com")

        elif "open coursera" in query:
            webbrowser.open("https://www.coursera.com")

        elif "open torrent" in query:
            webbrowser.open("https://1337x.unblocked.nz/")

        elif 'play some music' in query:
            music_dir = "C:\\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is: {strTime}")

        elif 'open vs' in query:
            vscode = "C:\\Users\\risha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscode)

        elif 'open downloader' in query:
            bit = "C:\\Users\\risha\\AppData\\Roaming\\BitTorrent\\BitTorrent.exe"
            os.startfile(bit)

        elif 'send mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receivers email id"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry rishabh bhai. I am not able to send this email")    