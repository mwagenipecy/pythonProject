import datetime
import re
from datetime import time
from time import strftime
import long_responses as lofrng

# import pywhatkit
import speech_recognition as sr
import pyttsx3
# import pywhatkit
import pyaudio


def message_probability(user_message, recognize_words, single_response=True, required_word=[]):
    message_certain = 0
    has_required_word = True

    # to recognize the message use for loop to check on it
    for word in user_message:
        if word in recognize_words:
            message_certain += 1
    percent = float(message_certain) / float(len(recognize_words))

    # for required word to be present in the loop
    for word in required_word:
        if word not in user_message:
            has_required_word = False
            break

    if required_word or single_response:
        return int(percent * 100)
    else:
        return print("nothing match")

def check_all_messages(message):
    highest_probability_list = {}

    def response(bot_response, list_of_words, single_response=True, required_word=[]):
        nonlocal highest_probability_list
        highest_probability_list[bot_response] = message_probability(message, list_of_words, single_response,
                                                                     required_word)

    # create responce
    response('hello!', ['hi', 'hey', 'hello', 'hey there', 'tsup', 'heyo'],
             required_word=['tsup','hello','hi'])
    response(" i \'m doing good", ['how', 'are', 'doing'],
             required_word=['how','doing'])
    response('it is '+strftime('%H:%M:%S %p')+ " \n can i help you more?" ,['time','day','your','whatch'],
             required_word=['time','day'])
    response('my name is kid p machine assistant person to help you',['name','who', 'are', 'you','your','name','where are you'],
             required_word=['name','who' ,'are', 'you','where are you','tell me'])
    response('Thank you! \n you are welcome....', ['thank' ,'thanks','you',' too','no','not', 'fine', 'understood'],
             required_word=['thank', 'fine', 'understood','no','thanks'])
    response('ooh! wow, i am very happy to meet you',['happy','my','name','see you','next', 'time'],
             required_word=['i','am','happy','to','meet','you','happy','see','you','meet','you','again','my','name'])
    response('welcome !',['okey','bye'], required_word=['okey','bye'])

    response('okay, welcome',['yes'], required_word=['yes'])

    response('see you too ',['see','you','once','again','next','time'],required_word=['see','you','once','again','next','time'])

    response(' it is AI program',['what','is','gpt'],required_word=['gpt','what','is'])

    response('Hapo na bado famchezo nini ',['nimechoka','mybolt','mbona','mateso','yamezidi'],required_word=['mybolt','nimechoka','i',' needfavor'])
    # creatint the  dictionary
    best_match = max(highest_probability_list, key=highest_probability_list.get)
    # print(highest_probability_list)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[10].id)
    engine.say(best_match)
    engine.runAndWait()
    return best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,:?!-.]\s', user_input.lower())
    response = check_all_messages(split_message)
    return response


def startConversationWithBolt():
    responce=input("Do you want to start conversation with bolt?")
    if "yes" in responce:
        name = input("what is your name")
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[10].id)
        engine.say('Welcome '+name)
        engine.runAndWait()
        while True:
          print("Breezy :" + get_response(input("you : ")))



    else:
        pass



print(startConversationWithBolt())




