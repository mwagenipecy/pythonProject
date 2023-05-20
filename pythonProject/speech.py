# import pywhatkit
import speech_recognition as sr
import pyttsx3
# import pywhatkit
import pyaudio

name = input("enter your name: ")

pyaudio.get_portaudio_version_text()

# include the voice mail on your code on the term of speaking on the different activities


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)
engine.say('Welcome ' + name)
engine.runAndWait()


# pywhatkit.playonyt('play diamond')
# pywhatkit.search('two lovers')




# def webdirective(message):
#     for word in message:
#         if "facebook" in word:
#             pywhatkit.search("www.facebook.com")
#         else:
#             pass
# webdirective('facebook account')

try:
    with sr.Microphone() as audio_source:
        engine = pyttsx3.init()
        get_audio = sr.Recognizer()
        print('speak now .......')
        voice = get_audio.listen(audio_source)
        command = get_audio.recognize_google(voice)
        engine.say("thanks wait for moment .")
        engine.runAndWait()
        # pywhatkit.playonyt(command)
        print("over..")

except:
    pass
