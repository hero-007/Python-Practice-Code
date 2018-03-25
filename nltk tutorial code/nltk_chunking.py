import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer as pst      # PunktSentenceTokenizer is a unsupervised machine learning sentence tokenizer. We can train it if we want but it comes pre-trained.


sample_text = state_union.raw("2006-GWBush.txt")
train_text = state_union.raw("2005-GWBush.txt")
custom_sent_tokenizer = pst(train_text)         # here we are creating a PunktSentenceTokenizer object and train it on train_text though it is not compulsory as the tokeniser comes pre trained.

tokenized = custom_sent_tokenizer.tokenize(sample_text)     # tokenizing the sample_text on the basis of sentences in sample_text


def process_content():
    for i in tokenized:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)

        chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}  """
        chunkParser = nltk.RegexpParser(chunkGram)
        chunked = chunkParser.parse(tagged)

        chunked.draw()

process_content()
