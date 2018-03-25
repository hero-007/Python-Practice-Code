# stemming : It is a form of data pre-processing. Main idea behind stemming is to consider the root stem of the part
# and remove the other part.        Ex - riding and ride - root stem = ride

# Reason for stemming - A word may have various form in a sentence but the various froms of the words have same meaning.
# Ex - I was taking a ride in a car.
# Ex - I was riding the car.
# Both the above sentences have same meaning but different form of word = 'ride'.
# so in order to reduce the space usage of these similar kind of words in the database we use stemming.


from nltk.stem import PorterStemmer             # there are multiple stemmer and we can even train our own stemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

ex_words = ['python','pythoner','pythoning','pythonly']

for w in ex_words:
    print(ps.stem(w))

# similarly we can stem an entire sentence
# stemming is not used much
