import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)      # adapt to the noise

    while True:
        audio = r.listen(source)

        # recognize the speech using Sphinx (Works Offline)
        try:
            print("You said :",r.recognize_google(audio))
        except:
            print("Sorry I couldn't listen\n")
