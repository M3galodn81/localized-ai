import requests
from bs4 import BeautifulSoup
import text_analzyer

def find_definition(word):
    results = None
    word = word.replace(' ','_')
    print(f'https://www.tagalog-dictionary.com/search?word={word}')
    f'https://tagalog.pinoydictionary.com/word/word/'
    response = requests.get(f'https://tagalog.pinoydictionary.com/word/{word}/')
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        results = soup.find('div', {'class': 'word-group'}).prettify()
    except AttributeError:
        print(f'{word} has no entry on the database')
    print(results)
 
find_definition('test')