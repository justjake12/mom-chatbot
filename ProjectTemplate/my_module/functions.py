"""A collection of functions for doing my project."""


import string
import nltk
import random

#MY OUTPUTS
BYE = ['I will talk to you later', 'Be safe', \
      'Call me after class', 'Adios mi amorcito']

ADVICE_IN = ['help', 'stressed', 'depressed', 'nervous', 'advice', 'anxious', 'sad', 'feeling down']

QUESTION_OUT = ["Oh honey, I don't know", "Let me ask Dad", "I'll just call you later"]

RANDOM = ['Oh okay', 'Call me when you can', 'What?', 'Sounds good', 'Watch your tone']

GREETING_IN = ['morning', 'hey', 'whatsup', 'hi', 'hello', 'hola', 'yo']
GREETING_OUT = ['Good morning, honey!', 'How are you?', \
                'yo yo yo', 'que pasa', \
                'I was just thinking about you', \
                'Dad and I were just talking about you']

HUMOR_IN = ['joke', 'haha', 'funny', 'lmao', 'lol']
HUMOR_OUT = ['you get your humor from me', \
            'dont be surprised. you know im the funny one', \
            'why was that funny?', 'what does that even mean']

LOVEY_IN = ['love', 'miss']
LOVEY_OUT = ['I love you more, sweetie', 'I miss you so much. Come home soon', \
            'Not as much as I love you']

HOW_IN = ['How are you?', 'How was your day?']
HOW_OUT = ['Im good, sweetie! Thanks for checking up on me', \
          'Everything is good so far today!', 'Better than yesterday, but still not great', \
          'Ugh Im a little frustrated but everything will pass!']


def prepare_text(input_string):

    """Function to take a string, and separate it into a list
    Code taken from A3"""
    temp_string = remove_punctuation(input_string.lower())
    out_list = temp_string.split()
    return(out_list)


def is_question(input_string):
 
    """ Function to determine if the input is a question or not
    Code from Assignment 3 to determine if the input is a question"""
    for item in input_string:
        if '?' in input_string:
            output = random.choice(QUESTION_OUT)
        else:
            output = random.choice(RANDOM)
        return(output)
    

    
def selector(input_list, check_list, return_list):

    """Function designed to check if a list of inputs is in the second list, and if so, a list of responses is ready
    Code From A3"""
    output = None
    for item in input_list:
        if item in input_list and item in check_list:
            output = random.choice(return_list)
    return(output)



def remove_punctuation(input_string):
    
    """
    Function designed to get rid of any punctuation in our input string
    Code From A3
    """
    out_string = ''
    for char in input_string:
        if char not in string.punctuation:
            out_string = out_string + char
    return(out_string)


def end_chat(input_list):
    
    """Function defined to end our chatbot if 'bye' comes in the input
    Code From A3"""
    if 'bye' in input_list:
        return(True)
    else:
        return(False)

    
def list_to_string(input_list, separator):

    """Function to combine a list of strings into one coherent string
    Code from A3"""
    output = input_list[0]
    for item in input_list[1:3]:
        output = string_concatenator(output, item, separator)
    return(output)



def string_concatenator(string1, string2, separator):
    
    """Function to combine multiple strings into one coherent string
    Code From A3"""
    output = string1 + separator + string2
    return(output)


def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two."""
    """CODE GIVEN TO US IN A3"""
    for element in list_one:
        if element in list_two:
            return True
    return False



def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise."""
    
    for element in list_one:
        if element in list_two:
            return element
    return None