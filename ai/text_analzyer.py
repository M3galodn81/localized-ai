import voice_input
from nltk.tokenize import word_tokenize
import datetime


months_en =['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months_tl =['Enero', 'Pebrero', 'Marso', 'Abril', 'Mayo', 'Hunyo', 'Hulyo', 'Agosto', 'Setyembre', 'Oktubre', 'Nobyembre', 'Disyembre']

def greeting():
    voice_input.speak('Hello')

def time_now():
    time = datetime.datetime.now()
    hour = time.strftime('%I:%M')
    if time.strftime('%p') == 'AM':
        meridiem = ' ng umaga'
    else:
        meridiem = ' ng hapon'
    output = hour + meridiem
    print(output)
    voice_input.speak(output)

def translate_month(month_en):
    i = months_en.index(month_en)
    return months_tl[i]
    
def date_now():
    time = datetime.datetime.now()
    month = translate_month(time.strftime('%B'))
    day = time.strftime('%d')
    year = time.strftime('%Y')
    output = f'Ika-{day} ng {month} ng taong {year}'
    print(output)
    voice_input.speak(output)

def token_analyze(query):
    tokens = word_tokenize(query)
    # tokens = 'Kamusta'
    tokens = [token.lower() for token in tokens]
    print(tokens)

    if 'hello' in tokens:
        print('hello')
        greeting()

    if ('ano' in tokens or 'anong' in tokens)  and 'oras' in tokens:
        print('time')
        time_now()

    if ('ano' in tokens or 'anong' in tokens) and 'petsa' in tokens:
        print('date')
        date_now()

    if 'close' in tokens and 'app' in tokens:
        print('exit')
        voice_input.speak('goodbye')
        return False

    if 'kamusta' in tokens:
        voice_input.speak('Kamusta ka rin')
        print('Tagalog greeting')
    
if __name__ == '__main__':
    token_analyze()