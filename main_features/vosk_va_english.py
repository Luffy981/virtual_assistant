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
from face_recog import face_analize
from speaker_verification import SpeakerVerification
import wave
from style_transfer import Streamming, Pick_Style, Show_Styles
from PIL import Image
from gif_animation import ImageLabel
import tkinter as tk
import threading

# SpeakerVerification = __import__("./speechbrain/speaker_verification").SpeakerVerification

listener = sr.Recognizer()

openai.api_key= openai_key



def input_command(command):
    # print(command)
    if 'hello elizabeth' in  command:
        # output('lala', 'moshi_moshi.mp3')
        output('Yes darling?... do you need something?')
    elif 'whatsapp' in command or "open what's up" in command:
        output('whatssap opened', 'ara_ara_uhuhu.mp3')
        sleep(1)
        os.system('whatsapp-for-linux &')
        output("whatsapp abierto")
    elif "close what's up" in command:
        print("clossing...")
        output("whatsapp closed")
        os.system('pkill -9 whatsapp-for-li')
    elif 'open email' in command:
        output('email opened', 'ara_ara_uhuhu.mp3')
        os.system('prospect-mail &')
        sleep(1)
        output("correo abierto")
    elif 'close email' in command:
        os.system('pkill -9 prospect-mail')
        output("correo cerrado")
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
        output(f'son {weat} grados Celcius en Lima')
    # if 'who is' in command:
                # wiki(command)
    elif 'joke' in command:
        output(pyjokes.get_joke())
    elif 'fuck you' in command:
        output('angry', 'angry.mp3')
    elif 'style transfer' in command:
        output('Taking photo...')
        Streamming()
        output('Choose the style you want apply')
        Show_Styles()
        command = get_audio_vosk()
        # print(command)
        command = command.split()[1]
        # print("SPLITTED " ,command)
        output('Applying style...')
        output('It takes a few minutes... please wait')
        Pick_Style(command)
    elif "i am good too" in command:
        output('sugoi', 'sugoi_sugoi.mp3')

    elif command != 'the':
        response = openai.Completion.create(engine="text-davinci-003",
                                            prompt=command,
                                            temperature=0.5,
                                            max_tokens=256,
                                            top_p=1,
                                            best_of=10,
                                            frequency_penalty=1.5,
                                            presence_penalty=1.5)
        print(response['choices'][0]['text'])
        output(response['choices'][0]['text'])
        # output(response)

def output(command, file='talk.mp3'):
    tts = gtts.gTTS(command, lang="en", tld="co.uk")
    tts.save(f"sounds/talk.mp3")
    playsound(f'sounds/{file}')

def grettings():
    hour = datetime.now().hour
    if hour >= 6 and hour < 12:
        output("Good morning darling, my name is Elizabeth", 'OhayouGozaimasu.mp3')
        # output("Good morning darling, my name is Elizabeth")
    elif hour >= 12 and hour < 18:
        output("Good afternoon darling", 'konichiwa.mp3')
        # output("Buenas tardes amo, mi nombre es Elizabeth")
    elif hour >= 18 or hour >= 0 and hour < 6:
        # output("Oyasumi nasai oniichan")
        output("Good afternoon darling", 'konichiwa.mp3')
        # output("Good night darling", 'oyasumi_chibi.mp3')
        # output("Buenas noches amo, mi nombre es Elizabeth")
    output("What can i do for you?")

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
model = Model(r"./model_english/")
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




CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
FILENAME = "output.wav"
def who_are_you():
    mic = pyaudio.PyAudio()
    # Open stream
    stream = mic.open(format=FORMAT,
                      channels=CHANNELS,
                      rate=RATE,
                      input=True,
                      frames_per_buffer=CHUNK)
    # stream.start_stream
    print("start recording...")
    frames = []
    seconds = 5
    for i in range(0, int(RATE/CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("recording stopped...")

    stream.stop_stream()
    stream.close()
    mic.terminate()


    wf = wave.open(FILENAME, "wb")
    wf.setnchannels(1)
    wf.setsampwidth(mic.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


class Assistant:
    def __init__(self):
        self.root = tk.Tk()
        self.label = ImageLabel(self.root)
        threading.Thread(target=self.run_assistant).start()
        self.label.pack()
        self.label.load('./girl_anime.gif')
        self.root.mainloop()


    def run_assistant(self):

        self.label.config(fg="red")
        output("Initializing voice recognition...")
        while True:
            self.label.config(fg="red")
            output("Who are you?")
            who_are_you()
            prediction = SpeakerVerification(FILENAME)

            if bool(prediction[0]) is False:
                self.label.config(fg="red")
                output("Voice recognition failed, please try again")
                continue
            else:
                self.label.config(fg="red")
                output("Voice test passed")
                break
    
        output("Initializing facial recognition...")

        while True:
            result = face_analize()
            if result:
                self.label.config(fg="red")
                output("Welcome darling...")
                break
            else:
                self.label.config(fg="red")
                output("Face recognition failed, please try again")
        grettings()

        while True:
            command = get_audio_vosk()
            print(command)
            if 'goodbye' in command:
                output('good bye darling, have a nice day')
                output('good bye', 'konichiwa_sayonara.mp3')
                self.label.config(fg="red")
                self.root.destroy()
                exit()
            else:
                input_command(command)


Assistant()
