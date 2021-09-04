from get_audio import get_audio
import wikipedia
import time
from gtts import gTTS
import wikipedia
import playsound
import os

# wikipedia.set_lang('en')
# language = 'en'
wikipedia.set_lang('vi')
language = 'vi'

def stop():
    TextToSpeech("See you later!",language)

def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            TextToSpeech("Can you say that again",language)
    time.sleep(2)
    stop()
    return 0


def TextToSpeech(text,language):
	#print("Bot: {}".format(text))
	tts = gTTS(text=text, lang=language, slow = False)
	tts.save("sound.mp3")
	playsound.playsound("sound.mp3", True)
	#song = AudioSegment.from_mp3("sound.mp3")
	#play(song)
	os.remove("sound.mp3")

#text = "Xin Chào mọi người"
a = get_text()
print(a)