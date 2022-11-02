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
from vosk import Model, KaldiRecognizer
import pyaudio
import openai
from apy_keys import openai_key, weather_key

listener = sr.Recognizer()

openai.api_key= openai_key


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
    print(command)
    if 'elizabeth' in  command:
        # output('lala', 'moshi_moshi.mp3')
        output('yes darling?... Do you need something?')
    elif 'what is your name' in command:
        output('my name is Elizabeth, nice to meet you')
    elif 'whatsapp' in command or "open what's up" in command:
        output('whatssap opened', 'ara_ara_uhuhu.mp3')
        sleep(1)
        os.system('whatsapp-for-linux &')
        output("whatsapp opened")
    elif "close what's up" in command:
        print("clossing...")
        output("whatsapp closed")
        os.system('pkill -9 whatsapp-for-li')
    elif 'open email' in command:
        output('email opened', 'ara_ara_uhuhu.mp3')
        os.system('prospect-mail &')
        sleep(1)
        output("email opened")
    elif 'close email' in command:
        os.system('pkill -9 prospect-mail')
        output("email closed")
    elif 'open discord' in command or 'open discourse' in command:
        output('email discord', 'ara_ara_uhuhu.mp3')
        os.system('discord &')
        sleep(1)
        output("discord opened")
    elif 'linkedin' in command:
        output('Linkedin opened', 'ara_ara_uhuhu.mp3')
        url = 'https://www.linkedin.com/feed/'
        webbrowser.get().open(url)
        sleep(1)
        output('Linkedin opened')
    elif 'facebook' in command:
        output('facebook opened', 'ara_ara_uhuhu.mp3')
        url = 'https://www.facebook.com/'
        webbrowser.get().open(url)
        sleep(1)
        output('facebook opened')
    elif 'open' in command:
        output("sorry I don't understand, could you repeat please?")
        return
    elif 'temperature' in command:
        weat = weather()
        output(f'it is {weat} degrees celsius in Lima')
    # if 'who is' in command:
                # wiki(command)
    elif 'joke' in command:
        output(pyjokes.get_joke())
    elif 'bye' in command or 'see you' in command:
        output('good bye', 'konichiwa_sayonara.mp3')
        exit()
    elif 'play music' in command:
        print("music play")
        play_music()
    elif 'next music' in command:
        print("next music")
        next_music()
    elif  'open files' in command:
        output('Tree file opened')
        tree_file()
    if 'fuck you' in command:
        output('angry', 'angry.mp3')
    elif "i'm fine too" in command:
        output('sugoi', 'sugoi_sugoi.mp3')
    elif command != 'the':
        response = openai.Completion.create(engine="text-davinci-002",
                                            prompt=command,
                                            temperature=0.1,
                                            max_tokens=256,
                                            top_p=1,
                                            best_of=2,
                                            frequency_penalty=0.4,
                                            presence_penalty=0.3)
        print(response['choices'][0]['text'])
        output(response['choices'][0]['text'])
        # output(response)

def output(command, file='talk.mp3'):
    tts = gtts.gTTS(command, lang="en", tld='co.uk')
    tts.save(f"sounds/talk.mp3")
    playsound(f'sounds/{file}')

def grettings():
    hour = datetime.now().hour
    if hour >= 6 and hour < 12:
        output("Good morning darling", 'OhayouGozaimasu.mp3')
        # output("Good morning darling, my name is Elizabeth")
    elif hour >= 12 and hour < 18:
        # output("Good afternoon darling", 'konichiwa.mp3')
        output("Good afternoon darling, my name is Elizabeth")
    elif hour >= 18 or hour >= 0 and hour < 6:
        # output("Oyasumi nasai oniichan")
        # output("Good night darling", 'oyasumi_chibi.mp3')
        output("Good night darling, my name is Elizabeth")
    output("What can i do for you?")

def check_new_email():
    email_list = {
            "test": "jhonsmith981@hotmail.com"
            }
    email = EmailMessage()

def weather():
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q":"lima"}

    headers = {
	    "X-RapidAPI-Key": weather_key,
	    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    print(response['current']['temp_c'])
    return response['current']['temp_c']


# Loading vosk model
model = Model(r"/home/luffy/holberton/virtual_assistant/model")
recognizer = KaldiRecognizer(model, 16000)


def get_audio_vosk():

    # Instantiate pyaudio
    mic = pyaudio.PyAudio()
    # Open stream
    stream = mic.open(format=pyaudio.paInt16,
                      channels=1,
                      rate=16000,
                      input=True,
                      frames_per_buffer=8192)
    stream.start_stream
    while True:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            dict_text = eval(text)
            if dict_text['text'] != "":
                # Stop stream
                stream.stop_stream()
                stream.close()
                # Close PyAudio
                mic.terminate()
                return dict_text['text']
grettings()
while True:
    command = get_audio_vosk()
    input_command(command)




