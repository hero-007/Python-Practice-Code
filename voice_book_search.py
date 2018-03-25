import speech_recognition as sr
import requests as rq

# function to parse the json obtained from google book api
def json_parser(dict):
    book_author = ''
    volumeInfo = dict['volumeInfo']
    book_name = volumeInfo['title']     # book name
    try:
        book_author = volumeInfo['authors'][0]  #book author
    except KeyError:
        book_author = 'Not Mentioned'
    return book_name,book_author

book_to_search = ''         # variable storing the book name

#obtain audio from the microphone

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)      #adapt to noise
    rox = -1

    while True and rox == -1:
        audio = r.listen(source)

        # recognize the speech using google (works online)

        try:
            print("Which book would you like me to search ???? ")
            book_to_search = r.recognize_google(audio)
            print("you said :",book_to_search)
            rox = 1
        except:
            print(" Which book do u want me to search ")
            pass

# now book_to_search contains name of the book
# using google book api to get the information regarding the book

base_url = 'https://www.googleapis.com/books/v1/volumes?q='
book_to_search = book_to_search.replace(' ','')
final_url = base_url+book_to_search
asr = rq.get(final_url)
json_object = asr.json()

# parsing the json object and showing the info user want to know

items = json_object['items']
print("$$$$$$$$$ TOTAL NUMBER OF RELEVANT BOOKS FOUND = "+str(len(items))+" $$$$$$$$$$")

book_count = 0

for item in items:
    book_name,book_author = json_parser(item)
    book_count+=1
    print(str(book_count)+'.',book_name)
    print("Book Author :",book_author,'\n\n') 

print("your final url : "+final_url)

input("$$$$$$$$$$$    PRESS ANY KEY TO EXIT THE PROGRAM   $$$$$$$$$$$$")
