import voice_input
from nltk.tokenize import word_tokenize
import datetime


months_en =['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months_tl =['Enero', 'Pebrero', 'Marso', 'Abril', 'Mayo', 'Hunyo', 'Hulyo', 'Agosto', 'Setyembre', 'Oktubre', 'Nobyembre', 'Disyembre']

def greeting():
    voice_input.speak('Hello rin.  Ako si Gabay ang inyong katulong')

def meridiem_tl():
    time = datetime.datetime.now()
    hr = int(time.strftime('%I'))
    md = time.strftime('%p')
    mn = int(time.strftime('%M'))

    if ((hr == 12) and (mn == 0) ) and (md == 'AM'):
        return 'ng hating-gabi'
    if (hr >= 5 and ((hr <= 11 )and (mn <= 59))) and (md == 'AM'):
        return 'ng umaga'
    if (hr >= 1 and ((hr <=5) and (mn <= 59))) and (md == 'PM'):
        return 'ng hapon'
    if (hr >= 6 and ((hr <=11) and (mn <= 59))) and (md == 'PM'):
        return 'ng gabi'
    if (hr >= 12 and ((hr <=12) and (mn <= 59))) and (md == 'PM'):
        return 'ng tanghali'
    if ((((hr >= 1) and (hr <= 4)) and ((mn >= 0) and (mn <= 59)) ) or ((hr ==12) and (mn >= 0) and (mn <= 59))) and  (md == 'AM'):
        return 'ng madaling araw'
    return None

def time_now():
    time = datetime.datetime.now()
    hour = time.strftime('%I:%M')
    meridiem = meridiem_tl()
    output = hour + ' '  +meridiem
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
    tokens = [token.lower() for token in tokens]
    print(tokens)

    if ('hello' in tokens ) and ('gabay' in tokens):
        print('AI: Greeting')
        greeting()

    if ('ano' in tokens or 'anong' in tokens)  and 'oras' in tokens:
        print('AI: Telling time')
        time_now()

    if ('ano' in tokens or 'anong' in tokens) and 'petsa' in tokens:
        print('AI: Telling date')
        date_now()

    if 'close' in tokens and 'app' in tokens:
        print('AI: Closing')
        voice_input.speak('Pa-alam, hanggang sa muli')

    if 'kamusta' in tokens:
        print('AI: Telling a tagalog greeting')
        voice_input.speak('Kamusta ka rin')

    if ('sino' in tokens) and ('nagdevelop' in tokens) and ('nito'in tokens):
        print('AI: Easter Egg')
        voice_input.speak('Ang gumagawa sa GABAY ay ang unang grupo ng STEM twelve - F')

        
    
if __name__ == '__main__':
    token_analyze()
