import pyaudio,os
import speech_recognition as sr
from datetime import datetime
#from .speech import Speech
from gtts import gTTS
from io import BytesIO
import pygame
import playsound
import time


chatbotcue = ["Chat Bot", "chatbot", "chat bot", "ChatBot", "jackpot", "jack pot", "Jack Pot" ]

def substring_after(s, delim):
    return s.partition(delim)[2]

def is_part_of_text_unique(text, string_list):
    for string in string_list:
        if string in text:
            return string
    return ""

def getTimeStampWithRoutineStep(text):
    print(text+":",datetime.now().strftime("%H:%M:%S"))
class Speech():

    @classmethod
    def speak(cls, text):
        mp3_file_object = BytesIO()
        tts = gTTS(text, lang='en')
        tts.write_to_fp(mp3_file_object)
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(mp3_file_object, 'mp3')
        pygame.mixer.music.play()
def mainfunction(source):
    try:
        audio = r.listen(source)
        getTimeStampWithRoutineStep("detecting Speech...")
        recognizedSpeech = r.recognize_google(audio,language = 'en-IN')
        print("recognizedSpeech: "+ recognizedSpeech)
        getTimeStampWithRoutineStep("finding cue...")
        reconnizedCue= is_part_of_text_unique(recognizedSpeech, chatbotcue)
        if (reconnizedCue != ""):
            getTimeStampWithRoutineStep("cue matched")
            #print(reconnizedCue)
            searchText =substring_after(recognizedSpeech, reconnizedCue)
            getTimeStampWithRoutineStep("parsed to get question")
            tts = gTTS(text=searchText, lang='en')
            filename = "abc.mp3"
            tts.save(filename)
            time.sleep(5)
            playsound.playsound('./'+filename)
            print('tried playing')
            os.remove(filename)
            getTimeStampWithRoutineStep("generating speech")
        else:
            getTimeStampWithRoutineStep("cue not found, exiting")
    except Exception as e :
        print('exception'+ e)

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            mainfunction(source)
