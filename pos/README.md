# nltk_project

# NLTK Stopwords and POS Tagging Project

This project demonstrates how to use the Natural Language Toolkit (NLTK) in Python to tokenize text, remove stop words, and perform part-of-speech (POS) tagging. The code takes a dummy text, tokenizes it into sentences and words, filters out stop words, and tags each word with its corresponding part of speech.

## Features

- **Sentence Tokenization:** Uses `sent_tokenize` to break text into sentences.
- **Word Tokenization:** Tokenizes each sentence into words.
- **Stop Words Removal:** Filters out common English stop words using NLTK's `stopwords` corpus.
- **POS Tagging:** Tags each word with its part of speech using NLTK's `pos_tag`.

## Installation

1. Install the required packages:
    ```bash
    pip install nltk
    ```

2. Download the necessary NLTK resources:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('averaged_perceptron_tagger')
    ```

## Usage

Here’s an example of how to run the script:

```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Set of stop words in English
stop_words = set(stopwords.words('english'))

# Dummy text
txt = "Sukanya, Rajib and Naba are my good friends. " \
      "Sukanya is getting married next year. " \
      "Marriage is a big step in one’s life." \
      "It is both exciting and frightening. " \
      "But friendship is a sacred bond between people." \
      "It is a special kind of love between us. " \
      "Many of you must have tried searching for a friend " \
      "but never found the right one."

# Tokenizing text into sentences
tokenized = sent_tokenize(txt)

# Loop through each sentence
for i in tokenized:
    # Tokenizing sentence into words
    wordsList = nltk.word_tokenize(i)

    # Removing stop words from wordsList
    wordsList = [w for w in wordsList if not w in stop_words]

    # POS Tagging words
    tagged = nltk.pos_tag(wordsList)

    print(tagged)
