import speech_recognition as sr
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("Welcome Mr. Stark")
var_exit = -1
while True:
    rs = sr.Recognizer()
    with sr.Microphone() as source:
        speaker.Speak("Please Wait while i calibrate the microphone, Won't take more than 2 second")
        rs.adjust_for_ambient_noise(source,duration=float(2))
        while True:
            speaker.Speak("What can I do for U Mr. Stark")
            audi = rs.listen(source)
            try:
                text_recieved = rs.recognize_google(audi)
                if audi.lower() == 'exit':
                    var_exit = 1
                    break
                
                speaker.Speak("You are telling me to "+audi)
                speaker.Speak("I'll try to complete the task")
            except:
                speaker.Speak("I didn't hear what you said")
                pass
        if var_exit == 1:
            break
speaker.Speak("Hope to see u soon Mr.stark")
    
                
            
