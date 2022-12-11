import voice_input
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import datetime


def greeting():
    voice_input.speak('Hello')

def time_now():
    time = datetime.datetime.now()
    output = time.strftime('%I%M%p')
    voice_input.speak(output)

def token_analyze(query):
    tokens = word_tokenize(query)
    tokens = [token.lower() for token in tokens]

    if 'hello' in tokens:
        print('hello')
        greeting()

    if 'what' in tokens and 'time' in tokens:
        print('time')
        time_now()

    

# print(word_tokenize(query))

# def preprocess(sent):
#     sent = nltk.word_tokenize(sent)
#     sent = nltk.pos_tag(sent)
#     return sent

# print(preprocess(query))

if __name__ == '__main__':
    token_analyze()