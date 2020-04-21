import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >=0 and hour<12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good Afternoon") 
    else:
        speak("Good Evening")

    speak("I am Optimus. Sir, please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception:
    
        print("say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("vipulagrawal716@gmail.com","cooooool")
    server.sendmail("vipulagrawal716@gmail.com",to,content)
    server.close()





if __name__ == "__main__":
    wishMe()
    #while True:

    if 1:
        query = takeCommand().lower()
        

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
           music_dir = 'C:\\Users\\Vipul Agrawal\\Music\\music\\audio'
           song = os.listdir(music_dir)
           print(song[0])  
           os.startfile(os.path.join(music_dir,song[0]))  

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Vipul Agrawal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'send email to vipul' in query:
            try:
                speak("what shoul i say")
                content = takeCommand()
                to = "agrawalvipul716@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend Vipul. I am not able to send this email")
