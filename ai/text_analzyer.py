import voice_input
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import datetime

meaning_stop_words = ['meaning','ibig','sabihin','nang','ng','anong','ano','ang']

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
    # web scrap it

def weather(text):
    # get location
    # check date and time then tell weather
    pass

def token_analyze(query):
    tokens = word_tokenize(query)
    tokens = [token.lower() for token in tokens]
    print(tokens)

    if 'hello' in tokens and not (any(x in meaning_stop_words for x in tokens)):
        print('hello')
        greeting()

    if 'what' in tokens and 'time' in tokens or 'oras' in tokens:
        print('time')
        time_now()

    if 'what' in tokens and 'date' in tokens or 'petsa' in tokens:
        print('date')
        date_now()

    if 'close' in tokens and 'app' in tokens:
        print('exit')
        voice_input.speak('goodbye')
        return False

    if 'kamusta' in tokens:
        voice_input.speak('Kamusta ka rin?')
        print('Tagalog greeting')
    
    if (any(x in meaning_stop_words for x in tokens)):
        search_words = []
        for x in range(len(tokens)):
            if not(tokens[x] in meaning_stop_words):
                search_words.append(tokens[x])
        search_key = ' '
        search_key = search_key.join(search_words)
        print('key: ' + search_key)

if __name__ == '__main__':
    token_analyze()