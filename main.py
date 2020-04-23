#!/usr/bin/python3
import speech_recognition as sr

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
            audio = r.listen(source=source, timeout=10, phrase_time_limit=5) 
        recognize_words = r.recognize_google(audio).lower().replace("'", "")
        print("Tadashi thinks you said '" + recognize_words + "'")
    except sr.UnknownValueError:
        listen = read_voice_cmd()
        return listen
    except sr.WaitTimeoutError:
        pass
    except sr.RequestError:
        print('FACING NETWORK ERROR!')
    return recognize_words

if __name__ == "__main__":
    recognize_words = voice_Recognizer()
    if 'hello' in recognize_words:
        print("hello sir")
    
   