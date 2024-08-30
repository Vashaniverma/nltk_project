# NLTK Chatbot Project

This project implements a simple rule-based chatbot using the Natural Language Toolkit (NLTK) in Python. The chatbot recognizes specific patterns in user inputs and provides predefined responses, making it a great introduction to natural language processing and chatbot development.

## Features

- **Pattern Matching:** The chatbot uses pattern matching with regular expressions to recognize user inputs and respond accordingly.
- **Reflections:** Implements simple reflection (e.g., changing "I am" to "you are") using the `reflections` dictionary from NLTK.
- **Predefined Responses:** The chatbot responds with predefined responses based on user input.
- **Fallback Response:** If the chatbot doesn't recognize a pattern, it provides a default fallback response.

## Installation

1. Install the required package:
    ```bash
    pip install nltk
    ```

2. Download the necessary NLTK resources:
    ```python
    import nltk
    nltk.download('punkt')
    ```

## Usage

Here’s how to run the chatbot:

```python
import nltk
from nltk.chat.util import Chat, reflections

# Define the pairs of patterns and responses
pairs = [
    # Example patterns and responses
    ['my name is (.*)', ['Hello %1!']],
    ['(hi|hello|hey|holla|hola)', ['Hey there!', 'Hi there!', 'Hey!']],
    ['(.*) your name ?', ['My name is chatbot.']],
    ['(bye|goodbye|see you later)', ['Goodbye!', 'See you later!', 'Take care!']],
    ['how are you ?', ['I am good, thank you!', 'I am doing well, how about you?']],
    ['(.*)', ['I am not sure I understand, could you please clarify?', 'Interesting, tell me more!']],
]

# Create a Chat object with the defined pairs and reflections
chat = Chat(pairs, reflections)

# Start the chatbot conversation
chat.converse()

Output
> hi
Hey there!

> what is your name?
My name is chatbot.

> how are you?
I am good, thank you!

> goodbye
Goodbye!
