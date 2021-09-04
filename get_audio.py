import speech_recognition as sr


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
            #print("Me: ", end='')
            audio = r.listen(source, phrase_time_limit=5)
            try:
                #text = r.recognize_google(audio, language="en-US")
                text = r.recognize_google(audio, language="vi-VN")
                #print(text)
                return  text
            except:
                #print("...")
                return  "..."