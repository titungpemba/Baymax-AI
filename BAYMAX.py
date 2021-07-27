#!/usr/bin/python3
import speech_recognition as sr
import datetime, time
import os, sys
import webbrowser
import pyttsx3
import re
import requests

r = sr.Recognizer()
   
def voice_Recognizer():
    recognize_words = ' '
    try:
        with sr.Microphone() as source:   
            print("Please wait. Calibrating microphone...")   
            # listen for 2 seconds and create the ambient noise energy level   
            r.adjust_for_ambient_noise(source, duration=2)  
            r.dynamic_energy_threshold = True    
            print("Listening...")  
            audio = r.listen(source) 
        recognize_words = r.recognize_google(audio).lower().replace("'", "")
        print("Baymax thinks you said '" + recognize_words + "'")
    except sr.UnknownValueError:
        listen = voice_Recognizer()
        return listen
    except sr.WaitTimeoutError:
        pass
    except sr.RequestError:
        print('FACING NETWORK ERROR!')
    return recognize_words

def speak(message):
    if sys.platform == 'darwin':
        tts_engine = 'say'
        return os.system(tts_engine + ' ' + message)
    elif sys.platform == 'win32':
        tts_engine = pyttsx3.init('sapi5')
        voices = tts_engine.getProperty('voices')
        # print(voices[1].id)
        tts_engine.setProperty('voice', voices[1].id)
        tts_engine.say(message)
        engine.runAndWait()
    elif sys.platform == 'Linux' or sys.platform == 'linux' or sys.platform == 'Ubuntu':
        #espeak
        tts_engine = 'espeak'
        print("Baymax: " + ' ' + message + '')
        return os.system(tts_engine + ' "' + message + '"')

def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("Hello I'm Baymax. Nice to meet you, how can I help you?")       

def date():
    currentdate = datetime.datetime.now()
    result = currentdate.strftime("%d %b %Y %A")
    print(result)
    speak(result)
    
def currenttime():
    result = time.strftime("%I:%M:%S %A")
    print(result)
    speak(result)

def googleSearch(recognize_words):
    cleanword = recognize_words.replace("ask google", "")
    webbrowser.open('https://www.google.com/search?q={}'.format(cleanword))
    result = 'Opening your query in google search engine sir'
    print(result)
    speak(result)

def location(recognize_words):
        data = recognize_words.split(" ")
        location = ""
        location = location.split(" ")
        for i in range(2, len(data)):
            location.append(data[i])
        place = "  ".join(location)
        result = "Hold on sir, I will show you."
        print(result)
        speak(result)
        webbrowser.open("https://www.google.nl/maps/place/" + place)

def openWebsite(recognize_words):
    reg_ex = re.search('open (.+)', recognize_words)
    if reg_ex:
        domain = reg_ex.group(1)
        url = "https://www." + domain + ".com"
        webbrowser.open(url)
        speak("done...")
    else:
        speak("website not exist")

def newsReport():
    apiKey = '49e391e7066c4158937096fb5e55fb5d'
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={apiKey}"
    r = requests.get(url)
    data = r.json()
    data = data["articles"]
    flag = True
    count = 0
    for items in data:
        count += 1
        if count > 10:
            break
        print(items["title"])
        to_speak = items["title"].split(" - ")[0]
        if flag:
            print("Today's top ten Headline are : ")
            speak("Today's top ten Headline are : ")
            flag = False
        else:
            print("Next news : ")
            speak("Next news : ")
        print(to_speak)
        speak(to_speak)
         
 #jokes function
         
 def jokes(recognize_words):
     res = requests.get('https://icanhazdadjoke.com/',headers={"Accept":"application/json"})
     if res.status_code == requests.codes.ok:
        jarvisResponse(str(res.json()['joke']))
        else:
            jarvisResponse('oops!I ran out of jokes)

if __name__ == "__main__":
    time.sleep(2)
    greeting()
    while True:
        recognize_words = voice_Recognizer()
        if "who are you" in recognize_words:
            print("I'm your Baymax a simple virtual assistant.")
            speak("I'm your Baymax a simple virtual assistant.")
        elif 'hello' in recognize_words:
            print("hello sir, how are you?")
            speak("hello sir, how are you?")
        elif "good morning" in recognize_words:
             print("good morning sir, Have a nice day!")
             speak("good morning sir, Have a nice day!")
        elif "good night" in recognize_words:
             print("good night sir, Sweet dreams")
             speak("good night sir, Sweet dreams")
        elif "how are you" in recognize_words:
            print("I'm not the only one here that's having fun with you, it's all me.")
            speak("I'm not the only one here that's having fun with you, it's all me.")
        elif "what's new" in recognize_words:
            print("Nothing. I just thought it was a bit of an overreaction. It's been a while since I've read it.")
            speak("Nothing. I just thought it was a bit of an overreaction. It's been a while since I've read it.")
        elif "it's good" in recognize_words:
            print("It's all good. It's one of those things that makes me smile")
            speak("It's all good. It's one of those things that makes me smile")
        elif "that's great" in recognize_words:
            print("Thank you")
            speak("Thank you")
        elif "thank you" in recognize_words:
            print("you're welcome")
            speak("you're welcome")
        elif "you are welcome" in recognize_words:
            print("my pleasure")
            speak("my pleasure")
        elif "where are you from" in recognize_words:
            print("Magical place call Nepal")
            speak("Magical place call Nepal")
        elif "who is your master" in recognize_words:
            print("PEMBA TAMANG, you can contact him through discord")
            speak("PEMBA TAMANG, you can contact him through discord")
        elif "goodbye" in recognize_words:
            print("See you later, bye")
            speak("See you later, bye")
            quit()
        elif "what is date" in recognize_words:
            date()
        elif "what is time" in recognize_words:
            currenttime()
        elif "ask google" in recognize_words:
            googleSearch(recognize_words)
        elif "where is" in recognize_words:
            location(recognize_words)   
        elif "open" in recognize_words:
            openWebsite(recognize_words)
        elif "what is the today headlines" in recognize_words:
            newsReport()
        #jokes
        elif "tell me joke" in reconginze_words:
              jokes(recognize_words)
