import voice_input
from nltk.tokenize import word_tokenize
import datetime


months_en =['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months_tl =['Enero', 'Pebrero', 'Marso', 'Abril', 'Mayo', 'Hunyo', 'Hulyo', 'Agosto', 'Setyembre', 'Oktubre', 'Nobyembre', 'Disyembre']

def greeting():
    voice_input.speak('Hello')

def meridiem_tl():
    hr = '%I'
    md = '%p'
    mn = '%M'
    if (hr == 12 ) and (md == 'AM'):
        return 'ng hating-gabi'
    if (hr >= 5 and (hr <=  11 and mn <= 59)) and (md == 'AM'):
        return 'ng umaga'
    if (hr >= 1 and (hr <=5 and mn <= 59)) and (md == 'PM'):
        return 'ng hapon'
    if (hr >= 6 and (hr <=11 and mn <= 59)) and (md == 'PM'):
        return 'ng gabi'
    if (hr >= 12 and (hr <=4 and mn <= 59)) and (md == 'PM'):
        return 'ng hapon'
    
    

def meridiem_tl():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    md = time.strftime('%p')
    mn = time.strftime('%M')

    hr = int(hr)
    mn = int(mn)

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
