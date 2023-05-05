'''TTS (Text to Speech)
STT (Speech to Text)'''

from gtts import gTTS
from playsound import playsound
f_name2 = "EngSci_eng.mp3"

# English Version
# text = "EngSci is the best program in the world. You should apply to EngSci."
# f_name1 = "EngSci.mp3"
# tts_english = gTTS(text = text, lang = "en")
# tts_english.save(f_name1)
# from playsound import playsound
# playsound(f_name1) # this will play the sound lol

# Korean Versin
# text = "엔지니어링 사이언스는 세계 최고의 프로그램입니다. 엔지니어링 사이언스에 지원하세요."
# # This is essentially same meaning as above in Eng version. 
# f_name2 = "EngSci_korean.mp3"
# tts_korean = gTTS(text = text, lang = "ko")
# tts_korean.save("EngSci_korean.mp3")
# # or 
# playsound(f_name2) # this will play the sound lol

with open('EngSci_eng.txt', 'r', encoding='utf-8') as f:
    text = f.read()
tts_korean = gTTS(text = text, lang = "ko")
tts_korean.save("EngSci_eng.mp3")
playsound(f_name2)

