from gtts import gTTS
import os 
import speech_recognition as sr

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    os.system('mpg123 ' + filename)
    os.system('rm' + filename)

def speak_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        print("RECOG:" + r.recognize_google(audio))
        speak(r.recognize_google(audio))
    except:
        print("Sorry could not recognize what you said")
        exit(0)
#wip makes audio work on linux
if __name__ == '__main__':
    speak_recognition()