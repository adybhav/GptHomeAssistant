import pyaudio,os
import speech_recognition as sr
from datetime import datetime
from speaker import TextToSpeech
from chatgptPi import RunGpt


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
            searchText =substring_after(recognizedSpeech, reconnizedCue)
            getTimeStampWithRoutineStep("parsed to get question")
            TextToSpeech(searchText)
            getTimeStampWithRoutineStep('tried playing')
            getTimeStampWithRoutineStep('running GPT')
            RunGpt(searchText)
            getTimeStampWithRoutineStep("generating speech")
        else:
            getTimeStampWithRoutineStep("cue not found, exiting")
    except Exception as e :
        print(e)

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            getTimeStampWithRoutineStep('waiting for input')
            mainfunction(source)
