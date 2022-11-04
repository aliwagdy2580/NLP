# import librarys

import re
import string
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')
from nltk import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
import nltk

"""#clean dataset"""

stop_words = stopwords.words('english')


def remove_non_ascii(text):
    """Remove non-ASCII characters from list of tokenized words"""
    return text.encode('ascii', 'ignore').decode()


def remove_brackets_num(text):
    return re.sub("\[.*?\]", "", text)


def to_lowercase(text):
    return text.lower()


def replace_numbers(text):
    """Replace all interger occurrences in list of tokenized words with textual representation"""
    return re.sub(r'\d+', '', text)


def remove_whitespace(text):
    return text.strip()


def remove_punctuation(text):
    punctuation = '''!()[]{};:'"\<>/?$%^&*_`~='''
    for punc in punctuation:
        text = text.replace(punc, "")
    return text


def remove_emails(text):
    return re.sub(r'[A-Za-z0-9]*@[A-Za-z]*\.?[A-Za-z0-9]*', "", text)


def text2words(text):
    return word_tokenize(text)


def remove_stopwords(words, stop_words):
    return [word for word in words if word not in stop_words]


def lemmatize_words(words):
    """Lemmatize words in text"""
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in words]




def NormalizeText(text):
  text = remove_non_ascii(text)
  text= remove_brackets_num(text)
  text = to_lowercase(text)
  #text=replace_numbers(text)
  text= remove_whitespace(text)
  text = remove_punctuation(text)
  text= remove_emails(text)
  words = text2words(text)
  #words = remove_stopwords(words, stop_words)
  #words = lemmatize_words(words)

  return ' '.join(words)

