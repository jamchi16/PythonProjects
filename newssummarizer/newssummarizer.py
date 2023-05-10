from bs4 import BeautifulSoup
from requests import get
import sys

url = "https://en.wikinews.org/wiki/Global_markets_plunge"

#if len(sys.argv) > 1:
    #url = sys.argv[1]
#else:
    #sys.exit("Error: Please enter the URL")

def get_only_text(url):
 page = get(url)
 soup = BeautifulSoup(page.content, "lxml")
 text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
 title = ' '.join(soup.title.stripped_strings)
 return title, text


text = get_only_text(url)

from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

print ("Title : " + text[0])
print ("Summary : ")
print (summarize(repr(text[1]), word_count=100))
int("\n\nLength of the summarized text: " + str(len(str.split((summarize(repr(text[1]), word_count=100))))))

print ("Title : " + text[0])
print ("Summary : ")
print (summarize(repr(text[1]), ratio=0.1))

summarized_text = summarize(repr(text[1]), ratio=0.1)

len(str.split(summarized_text))

print ('\nKeywords:')
print (keywords(text[1], ratio=0.1, lemmatize=True))



