from gtts import gTTS
import os
stk = input('Enter a text to convert to speech : ')
tts = gTTS(text=stk, lang='en')
tts.save("good2.mp3")
os.system(r'E:\good2.mp3')
