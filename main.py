from gtts import gTTS
import os 
import speech_recognition as sr
import datetime

r = sr.Recognizer
keywords = [("xanteres", 1), ("hey xanteres", 1), ]
source = sr.Microphone()

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    os.system('mpg123 ' + filename)
    os.system('rm' + filename)

def callback(recognizer, audio):
    try:
        speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=keywords)
        print(speech_as_text)
        if "xanteres" in speech_as_text or "hey xanteres":
            speak("Yes sir?")
            recognize_main()
    except sr.UnknownValueError:
        print("Please say it again")

def start_recognizer():
    print("Waiting for a keyword...Xanteres or Hey Xanteres")
    r.listen_in_background(source, callback)
    time.sleep(100000000)

def recognize_main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        data.lower()
        print("You said: " + data)
        if "how are you" in data:
            speak("I'm Good")
        elif "hello" in data:
            speak("Hello sir")
        else:
            speak("I am sorry, I did not understand your requests")
    except sr.UnknownValueError:
        print("Xanteres did not understand your requests")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

while 1:
    start_recognizer()