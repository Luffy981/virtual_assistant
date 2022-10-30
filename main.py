#!/usr/bin/env python3
import speech_recognition as sr
import pyttsx3
from datetime import datetime
from email.message import EmailMessage
from time import sleep
import os
import requests
import wikipedia
import pyjokes
import webbrowser
import pyautogui
import gtts
from playsound import playsound

listener = sr.Recognizer()

def get_audio():
    with sr.Microphone() as source:
        print("listening...")
        voice = listener.listen(source)
        command = ''
        try:
            command = listener.recognize_google(voice)
            command = command.lower()
        except:
            get_audio()
    return command
def input_command(command):
    try:

            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            print(voices[17].id)
            print(voices[20].id)
            engine.setProperty('voice', voices[17].id)
            if 'alexa' in  command:
                command = command.replace('alexa', '')
                print(command)
            if 'open whatsapp' in command:
                output('Linkedin opened', 'ara_ara_uhuhu.mp3')
                os.system('whatsapp-for-linux')
                print(command)
            if 'open email' in command:
                os.system('prospect-mail')
                engine.say('email abierto')
                print(command)
            if 'weather' in command:
                weat = weather()
                engine.say(f'son {weat} grados celcius en Lima')
            if 'who is' in command:
                wiki(command)
            if 'joke' in command:
                output(pyjokes.get_joke())
            if 'open linkedin' in command:
                output('Linkedin opened', 'ara_ara_uhuhu.mp3')
                url = 'https://www.linkedin.com/feed/'
                webbrowser.get().open(url)
            if 'bye' in command or 'see you' in command:
                output('good bye', 'konichiwa_sayonara.mp3')
                exit()
            if 'play music' in command:
                print("music play")
                play_music()
            if 'next music' in command:
                print("next music")
                next_music()
            if  'open files' in command:
                output('Tree file opened')
                tree_file()
            if 'f*** you' in command:
                output('angry', 'angry.mp3')


            engine.runAndWait()
            print(command)
    except Exception as e:
        print("Error: ", e)
        pass

# def output(out):
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[17].id)
#     engine.setProperty("rate", 180)
#     engine.say(out)
#     engine.runAndWait()
#     print(out)

def output(command, file='talk.mp3'):
    tts = gtts.gTTS(command, lang="en", tld='co.uk')
    tts.save(f"sounds/talk.mp3")
    playsound(f'sounds/{file}')

def grettings():
    hour = datetime.now().hour
    if hour >= 6 and hour < 12:
        output("Good morning master", 'oyasumi_chibi.mp3')
    elif hour >= 12 and hour < 18:
        output("Good afternoon master", 'konichiwa.mp3')
    elif hour >= 18 or hour >= 0 and hour < 6:
        # output("Oyasumi nasai oniichan")
        output("Good morning master", 'OhayouGozaimasu.mp3')

def check_new_email():
    email_list = {
            "test": "jhonsmith981@hotmail.com"
            }
    email = EmailMessage()

def weather():
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q":"lima"}

    headers = {
	    "X-RapidAPI-Key": "1b07469516mshcd6b8c9d4cb0ff8p1336b3jsn6d9658bb991a",
	    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    print(response['current']['temp_c'])
    return response['current']['temp_c']

def wiki(command):
    person = command.replace('who is', '')
    info = wikipedia.summary(person, 1)
    print(info)
    output(info)

def play_music():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('p')
    pyautogui.keyUp('p')
    pyautogui.keyUp('alt')

def next_music():
    pyautogui.keyDown('shift')
    pyautogui.keyDown('alt')
    pyautogui.keyDown('n')
    pyautogui.keyUp('n')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('shift')

def tree_file():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('f')
    pyautogui.keyUp('f')
    pyautogui.keyUp('ctrl')
grettings()
# output('I am Thoru ... What can i do for you?')
while True:
    output('listening...')
    command = get_audio()

    input_command(command)



