import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("I am listining...") # To check if the program is working
    audio = r.listen(source) # listen for the first phrase and extract it into audio data
    print("Recognizing...") # Also, checking if it works

try:
    # Google API using, and this is limited to 50 requests per day
    # so don't test it too much
    text = r.recognize_google(audio, language = "ko")
    # remember you gotta speak in korean to use this lol
    # if you want to speak in English, change the language to "en"
    # e.g) text = r.recognize_google(audio, language = "en-US")
    # Also you can test urself if ur pronunciation is correct or not
    print(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Request Failed; {0}".format(e)) # API key error or network error or whatever

