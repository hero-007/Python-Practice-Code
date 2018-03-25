import speech_recognition as sr
from os import listdir,chdir
from os.path import join,isfile

chdir(r'C:\Users\HP\Desktop\Satya work')
my_path = r'C:\Users\HP\Desktop\Satya work'

f = open('paper.txt','w')

audio_file_list = listdir(my_path)
audio_list = []
for i in audio_file_list:
    fl = join(my_path,i)
    if isfile(fl):
        audio_list.append(fl)


        
for j in range(1,len(audio_list),1):
    AUDIO_FILE = audio_list[j]
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file


    try:
        response =  r.recognize_google(audio)
        print(response,'\n',file = f)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

f.close()
