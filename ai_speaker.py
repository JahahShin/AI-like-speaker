import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# Speech to Text (STT)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language = "ko")
        print("You said: " + text)
        answer(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e)) # API key error or network error or whatever

# Response 
def answer(input_text):
    answer_text = ""
    if "안녕" in input_text:
        answer_text = "안녕하세요. 저는 인공지능 스피커입니다."
    elif "날씨" in input_text:
        answer_text = "오늘 비씨주의 날씨는 매우 맑음입니다"
    elif "엔지니어링 사이언스" in input_text:
        answer_text = "엔지니어링 사이언스는 세계 최고의 프로그램입니다. 엔지니어링 사이언스에 지원하세요."
    elif "지민" in input_text:
        answer_text = "지민은 최고의 프로그래머입니다."
    elif "잘가" in input_text:
        answer_text = "안녕히 계세요"
        stop_listening(wait_for_stop=False)
        os._exit(0)
    else:
        answer_text = "Sorry, I am not trained to answer this question yet."
    speak(answer_text)

# Speech (TTS)
def speak(text):
    print("[AI] " + text)
    f_name = "voice.mp3"
    tts = gTTS(text = text, lang = "ko")
    tts.save(f_name)
    playsound(f_name)
    if os.path.exists(f_name):
        os.remove(f_name)

r = sr.Recognizer()
m = sr.Microphone() # Microphone class
speak("what can I do for you?")
stop_listening = r.listen_in_background(m, listen) 
# listen for the first phrase and extract it into audio data
while True:
    time.sleep(0.1) # sleep the loop for 0.1 seconds

# stop_listening(wait_for_stop=False)

# calling this function requests that the background listener
# stop listening

