import requests
from bs4 import BeautifulSoup
import string

punctuation = string.punctuation

f = open("ai/transcripts.txt","r")

words_line = []
no_of_words = []

for x in f:
    words_line.append(x)
    no_of_words.append(len(x.split()))
f.close()

words_punctuation = [audio_transcript.split() for audio_transcript in words_line]
words = [[word.strip(punctuation) for word in x] for x in words_punctuation ]
words = [word for sublist in words for word in sublist]
unique_words = set(words)
unique_words = sorted(list(unique_words))
print((unique_words))

definition_words = {key: '' for key in unique_words}

# for key in definition_words:
#     response = requests.get(f'https://www.tagalog-dictionary.com/search?word={key}')
#     soup = BeautifulSoup(response.text, 'html.parser')
#     results = soup.find_all(id_='tag_content')

for key in definition_words:
    definition_words[key] = f'https://www.tagalog-dictionary.com/search?word={key}'

print(definition_words)