# part of speech tagging : This is a part of pre-processing. Its labeling to every word, which part of speech it is.
# there are 8 parts of speech in english : noun,pronoun,verb,adverb,adjective,conjunction,preposition,interjection.

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer as pst      # PunktSentenceTokenizer is a unsupervised machine learning sentence tokenizer. We can train it if we want but it comes pre-trained.


sample_text = state_union.raw("2006-GWBush.txt")
train_text = state_union.raw("2005-GWBush.txt")
custom_sent_tokenizer = pst(train_text)         # here we are creating a PunktSentenceTokenizer object and train it on train_text though it is not compulsory as the tokeniser comes pre trained.

tokenized = custom_sent_tokenizer.tokenize(sample_text)     # tokenizing the sample_text on the basis of sentences in sample_text


def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
        print(str(e))

process_content()


# nltk.help.upenn_tagset()
# is used to find all the speec-tag present in nltk
