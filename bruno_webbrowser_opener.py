import speech_recognition as sr
import webbrowser as wb
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

active_check = False
task_complete_check = -1
while True and task_complete_check == -1:
    if active_check == False:
        active_text = 'bruno'
        rs = sr.Recognizer()
        with sr.Microphone() as source:
            print("########## BRUNO IS INACTIVE ###########")
            print("****** CALIBARATING NOISE LEVEL******")
            rs.adjust_for_ambient_noise(source,duration=float(2))
            roxy = -1
            while True and roxy == -1:
                print("****** CALIBARATING NOISE LEVEL******")
                rs.adjust_for_ambient_noise(source,duration=float(2))
                print("Speak to activate bruno ")
                audi = rs.listen(source)
                print("DONE RECORDING")

                try:
                    print("SENDING DATA TO API")
                    text_recieved = rs.recognize_google(audi)   
                    print("DATA RECIEVED")
                    if text_recieved.lower() == 'bruno':
                        active_check = True
                        roxy = 1
                    else:
                        pass
                except:
                    print("Bruno is still Inactive")
                    pass
                
        
    else:
        speaker.Speak("Welcome Mr Stark, What can I do for U")
        text_to_search = ' '
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("***** CALIBARATING THE NOISE LEVEL *******")
            r.adjust_for_ambient_noise(source,duration=float(2))      # adapt to the noise
            rox = -1 
            while True and rox == -1:
                speaker.Speak("What would you like to watch on youtube")
                audio = r.listen(source)
                print("DONE RECORDING")

                # recognize the speech using Sphinx (Works Offline)
                try:
                    print("\n SENDING THE RECORDING TO API")
                    text_to_search = r.recognize_google(audio)
                    print("\n DATA RECIEVED ")
                    rox = 1
                except:
                    speaker.Speak("What do u want me to do")
                    pass

        if task_complete_check == -1:
            wb.open('https://www.youtube.com/results?search_query='+text_to_search)
            task_complete_check = 1
            break
        else:
            print('cannot perform this operation :',text_to_search)

input("********** PRESS ANY KEY TO EXIT THE PROGRAM **********")
