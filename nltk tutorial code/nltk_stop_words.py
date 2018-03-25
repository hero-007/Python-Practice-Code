# Stop Words : these are those words which do not contribute anything in the meaning of the text and can be ignored.
# they may make sense in genral language but when it comes to data analysis they are useless.
   # Ex - a,the,and etc

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = 'this is an example showing stop word filtration.'
stop_words = set(stopwords.words("english"))        # stopwords has few languages as stop words are diff for diff languages here we have used 'english' as lang
# print(stop_words)                                   # this will print all the stop words in english language

words = word_tokenize(text)

filtered_words = [] 

for w in words:
    if w not in stop_words:
        filtered_words.append(w)
        
print(filtered_words) 



# above code can also be written as from : filtered_words

# filtered_words = [w for w in words if not w in stop_words]
# print(filtered_words)



# Removing stop words from the sentence or paragraph can save lot of processing time.
# as these words do not contribut anything in the meaning of the paragraph or a sentence
