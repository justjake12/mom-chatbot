"""Test for my functions."""

from functions import list_to_string

def test_function():
    
    test_list = ['blah blah', 'hah', 'testing']
    testing1 = list_to_string(test_list, '~~')
    
    assert testing1 == 'blah blah~~hah~~testing'