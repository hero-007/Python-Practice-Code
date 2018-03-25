import speech_recognition as sr
import webbrowser as wb

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
        print("****** BRUNO : WHAT CAN I DO FOR YOU MY MASTER *******")
        text_to_search = ' '
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("***** CALIBARATING THE NOISE LEVEL *******")
            r.adjust_for_ambient_noise(source,duration=float(2))      # adapt to the noise
            rox = -1 
            while True and rox == -1:
                print("SPEAK 'WEB BROWSER' : \n")
                audio = r.listen(source)
                print("DONE RECORDING")

                # recognize the speech using Sphinx (Works Offline)
                try:
                    print("\n SENDING THE RECORDING TO API")
                    text_to_search = r.recognize_google(audio)
                    print("\n DATA RECIEVED ")
                    rox = 1
                except:
                    print("What do u want me to do")
                    pass

        if text_to_search in "web browser":
            wb.open('https://www.google.co.in/?gfe_rd=cr&dcr=0&ei=1WFCWuKLH4HT8gfWwIvwBQ')
            task_complete_check = 1
            break
        else:
            print('cannot perform this operation :',text_to_search)

input("********** PRESS ANY KEY TO EXIT THE PROGRAM **********")
