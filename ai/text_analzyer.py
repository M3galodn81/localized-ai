import voice_input
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import datetime

def greeting():
    voice_input.speak('Hello')

def time_now():
    time = datetime.datetime.now()
    output = time.strftime('%I%M%p')
    voice_input.speak(output)

def date_now():
    time = datetime.datetime.now()
    output = time.strftime('%B %d %Y')
    voice_input.speak(output)

def meaning(text):
    text = text.split()
    # remove any words before 'meaning' or anong ibig sabihin
    # add the words after the 'meaning' into a variable
    # search the defintion of the word
    # 

def token_analyze(query):
    tokens = word_tokenize(query)
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
    
    if 'meaning' in tokens:
        print('def')

if __name__ == '__main__':
    token_analyze()