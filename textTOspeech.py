from gtts import gTTS
import wikipedia
#from pydub import AudioSegment
#from pydub.playback import play
import playsound
import os

# wikipedia.set_lang('en')
# language = 'en'
wikipedia.set_lang('vi')
language = 'vi'
def TextToSpeech(text):
	#print("Bot: {}".format(text))
	tts = gTTS(text=text, lang='vi', slow = False)
	tts.save("sound.mp3")
	playsound.playsound("sound.mp3", True)
	#song = AudioSegment.from_mp3("sound.mp3")
	#play(song)
	os.remove("sound.mp3")
