import voice_input
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


# query = voice_input.take_command().lower()
query = voice_input.take_command()
print(word_tokenize(query))

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

print(preprocess(query))