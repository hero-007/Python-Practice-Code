import requests as rq


# create a function json_parser(dict) that take input as a dictionary and returns a tuple containig bookname,authorname and page count

def json_parser(dict):
    book_author = ''
    volumeInfo = dict['volumeInfo']
    book_name = volumeInfo['title']     # book name
    try:
        book_author = volumeInfo['authors'][0]  #book author
    except KeyError:
        book_author = 'Not Mentioned'
    return book_name,book_author

#forming the url and asking the user to enter the name of the book that user want to search

base_url = 'https://www.googleapis.com/books/v1/volumes?q='
book_to_search = input('Enter the name of the book : ')
book_to_search = book_to_search.replace(' ','%20')
final_url = base_url+book_to_search
asr = rq.get(final_url)
json_object = asr.json()

#parsing the json object and showing the info that user want to know

items = json_object['items']
print("$$$$$$$$$ TOTAL NUMBER OF RELEVANT BOOKS FOUND = "+str(len(items))+" $$$$$$$$$$")

book_count = 0

for item in items:
    book_name,book_author = json_parser(item)
    book_count+=1
    print(str(book_count)+'.',book_name)
    print("Book Author :",book_author,'\n\n')

input("$$$$$$$$$$$    PRESS ANY KEY TO EXIT THE PROGRAM   $$$$$$$$$$$$")
