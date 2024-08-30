import nltk
from nltk.chat.util import Chat, reflections 
  
pairs = [
    # Pattern: "my name is [something]", Response: "Hello [captured name]!"
    ['my name is (.*)', ['Hello %1!']],
    
    # Pattern: Greetings, Responses: Different greeting responses
    ['(hi|hello|hey|holla|hola)', ['Hey there!', 'Hi there!', 'Hey!']],
    
    # Pattern: "what is your name?", Response: "My name is chatbot"
    ['(.*) your name ?', ['My name is chatbot.']],
    
    # Pattern: Farewell, Responses: Different goodbye responses
    ['(bye|goodbye|see you later)', ['Goodbye!', 'See you later!', 'Take care!']],
    
    # Pattern: "how are you?", Responses: Different responses
    ['how are you ?', ['I am good, thank you!', 'I am doing well, how about you?']],
    
    # Pattern: Anything else, Response: Default fallback response
    ['(.*)', ['I am not sure I understand, could you please clarify?', 'Interesting, tell me more!']],
]

chat = Chat(pairs, reflections) 
chat.converse() 
