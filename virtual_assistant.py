import speech_recognition as srec

listen = srec.Recognizer()
with srec.Microphone() as source:
    print("Mendengarkan.......")
    voice = listen.listen(source, phrase_time_limit = 5)

    try:
        print("Diterima")
        print(listen.recognize_google(voice, language='id-ID'))
    except:
        pass