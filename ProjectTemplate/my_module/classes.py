"""A collection of classes for doing my project."""

import string
import nltk
import random


class Sibling():
    
    """Class to call on responses if a sibling is mentioned """
    """ORIGINAL CLASS CODE"""
    
    SIBLING_OUT = ['They are at school', 'They lost their privileges, so can you please talk to them', \
                  'I dont know how to handle your sibling getting in a fight', \
                  'We are gonna have a movie night! Wish you could be here']
    
    def respond(self):
        random.choice(self.SIBLING_OUT)
        
        
class Father():
    

    """Class to call on responses if the dad is mentioned"""
    """ORIGINAL CLASS CODE"""
    
    DAD_OUT = ['Why dont you call him?', 'He wont admit how much he misses you', \
              'He has been in a mood all day long, so I am hoping he will cheer up if you call him']
    
        
    def respond_dad(self):
        random.choice(self.DAD_OUT)
        
        
        
class Advice():
    
    """Class to call on responses if advice is needed"""
    """ORIGINAL CLASS CODE"""
    
    ADVICE_OUT = ['Can someone at school help you?', 'Want me to call you?', \
                 'Oh, honey. I am sorry you are not feeling the best right now. Try and take a break to relax, because you will help no one by stressing out right now', \
                 'How can I help you, baby?', 'Tell me what I can do to help you', 'Want me to come down there?']
    
    def respond_advice(self):
        random.choice(self.ADVICE_OUT)