from nltk.tokenize import sent_tokenize,word_tokenize

# tokenizer are of 2 types - 1> word tokenizer and 2> sentence tokenizer
# 1> Word tokenizer - seprates a paragraph in form of various words in it.
# 2> Sentence tokenizer - separates the paragraph in form of various sentences in the paragraph

# Lexicon and Corpora
# Corpora - is nothing but just a body of text containing similar kind of data. Ex - Crorpora of medical journals
# Lexicon - is like a dictionary i.e, words and there meanings. Words may have different meaning for different persons.
    # Ex - bull - for an investor it means a person who is positive about the market
    # Ex - bull - for a normal person means an animal with horns

    
text = 'hello there, how are you. how are you doing today? the wheather is great and Python is awsome.'
print(sent_tokenize(text))
print(word_tokenize(text))
