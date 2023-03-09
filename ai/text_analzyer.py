import voice_input
from nltk.tokenize import word_tokenize
import datetime


def greeting():
    voice_input.speak('Hello')

def time_now():
    time = datetime.datetime.now()
    output = time.strftime('%I%M%p')
    print(output)
    voice_input.speak(output)

def date_now():
    time = datetime.datetime.now()
    output = time.strftime('%B %d %Y')
    print(output)
    voice_input.speak(output)

def token_analyze(query):
    tokens = word_tokenize(query)
    # tokens = 'Kamusta'
    tokens = [token.lower() for token in tokens]

    if 'hello' in tokens:
        print('hello')
        greeting()

    if 'what' in tokens and 'time' in tokens:
        print('time')
        time_now()

    if 'what' in tokens and 'date' in tokens:
        print('date')
        date_now()

    if 'close' in tokens and 'app' in tokens:
        print('exit')
        voice_input.speak('goodbye')
        return False

    if 'kamusta' in tokens:
        voice_input.speak('Kamusta ka rin?')
        print('Tagalog greeting')
    

# print(word_tokenize(query))

# def preprocess(sent):
#     sent = nltk.word_tokenize(sent)
#     sent = nltk.pos_tag(sent)
#     return sent

# print(preprocess(query))

if __name__ == '__main__':
    token_analyze()