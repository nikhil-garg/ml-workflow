"""
Created on Wed Sep 12 2018

@author: Fabien Tarrade fabien.tarrade@axa.ch
"""
import re
import numpy as np
import pandas as pd
import nltk
from langdetect import detect

# sample functions based on an acutal project (NLP project)

def get_nb_sentence(text):
    """
    return the number of sentence in the text using nltk.sent_tokenize

    Args:
        text (str): input text

    Returns:
         float: number of sentence, NaN if None or NaN as input text
    """
    if not pd.isna(text):
        return len(nltk.sent_tokenize(text))
    else:
        return np.nan


def get_nb_token(text):
    """
    return the number of token in the text using nltk.word_tokenize(text)

    Args:
        text (str): input text

    Returns:
         float: number of token, NaN if None or NaN as input text
    """
    if not pd.isna(text):
        return len(nltk.word_tokenize(text))
    else:
        return np.nan


def anonymization(df):
    """
    does basic anonymization of client data

    Args:
        df: dataframe
    Return:
        dataframe with new anonymized variable (str)
    """

    anliegen_clear = df['text']
    if '\n' in anliegen_clear:
        anliegen_clear = anliegen_clear.replace('\n', '')
    anliegen_clear = anliegen_clear.lower()
    return anliegen_clear


def clean_up(text):
    """
    does clean up of special characters, punctuation and numbers
    Example for replacing countries

     Args:
        text:

    Return:
        dataframe with new cleaned variable (str)
    """
    text = re.sub('\d+', ' ', text)
    text = re.sub('\W+', ' ', text)
    text = re.sub(' . ', ' ', text)
    laender = re.finditer(
        '(Deutschland|Germany|Allemagne|Germania|Italien|Italy|Italie|Italia|Frankreich|France|Francia|Österreich|Oesterreich|Autriche|Austria)',
        str(text), re.IGNORECASE)
    for match in laender:
        text = text.replace(' ' + str(match.group()) + ' ', 'ausland')


def text_process(text, nlp, stopwords, language='de', mode='lemmatizing', number=True, email=True):
    """
    Apply NLP procedures to text.

    Parameters
    ----------
    text :  input text
	
    nlp :
	
    stopwords : list of stopwords
	
    language : de, fr, it, en
	
    mode : lemmatizing or stemming
	
    number :
	
    email :
	
    Returns
	-------
	stemmed/lemmatized tokens

    Lemmatizing and Stemming are not consistent yet. Lemmatizing removes e-mail addresses,
    numbers, punctuation which Stemming can't.
    """
    if mode == 'lemmatizing':
        doc = nlp(text.lower())
        tokens = [token.lemma_.lower() for token in doc if not
                  ((token.lemma_ in stopwords) or token.is_punct or token.is_quote or (
                      (token.is_digit or token.like_num) and number)
                   or (token.like_email and email))]

    if mode == 'stemming':
        if language == 'de':
            stemmer = nltk.stem.snowball.GermanStemmer(ignore_stopwords=False)
            language_nltk = 'german'
        elif language == 'fr':
            stemmer = nltk.stem.snowball.FrenchStemmer(ignore_stopwords=False)
            language_nltk = 'french'
        elif language == 'it':
            stemmer = nltk.stem.snowball.ItalianStemmer(ignore_stopwords=False)
            language_nltk = 'it'
        elif language == 'en':
            stemmer = nltk.stem.snowball.EnglishStemmer(ignore_stopwords=False)
            language_nltk = 'english'
        else:
            print("Language not recognized in text_preprocessing.")
            exit()
        # tokenize
        tokens = nltk.word_tokenize(text)

        # drop all token that are non character only and put everything in lower case
        tokens = [w.lower() for w in tokens if w.isalpha()]

        # remove stopwords
        stop = stopwords.words(language_nltk)

        tokens = [token for token in tokens if token not in stop]

        tokens = [stemmer.stem(token) for token in tokens]

    return " ".join(tokens)


def detect_language(text, lang='en'):
    """
    Detect the language of the given text.
    One may also pass a default language in case a not supported language is recognized.

    Parameters
    ----------
    text :
	
    lang : default language, default 'en'
	
    Returns
	-------
	detected language
    """
    list_lang = ['de', 'fr', 'it', 'en']
    try:
        language = detect(text)

        if (language not in list_lang) or (len(text) < 80):
            language = lang

    except Exception as ex:
        print('Exception with language detection: {0}'.format(str(ex)))

    return language
