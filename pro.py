import urllib

def read_text():
    quotes = open(r"C:\Users\HP\Desktop\tv series\test_file.txt")
    content_of_file = quotes.read()
    quotes.close()
    check_profanity(content_of_file)
    return

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    connection.close()
    if output=='true':
        print "Profanity Alert!!"
    elif output=='false':
        print "No curse word"
    else:
        print "Could not scan the doc!!"
    return

read_text()
