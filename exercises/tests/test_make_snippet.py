from lib.make_snippet import make_snippet
"""
Given a string that has more than 5 words 
returns the first 5 words then "..." 
"""
def test_given_a_string_with_more_than_5_words_returns_first_5_words():
    string = "A man who thinks all the time has nothing to think about except thoughts"    
    result = make_snippet(string)
    assert result == "A man who thinks all..."

"""
Given a string has 5 words 
returns the 5 words
"""
def test_given_a_string_with_5_words_returns_5_words():
    string = "I am a happy person"    
    result = make_snippet(string)
    assert result == "I am a happy person"

"""
Given a string has less then 5 words
return the words without "..."
"""
def test_given_a_string_with_less_than_5_words_returns_words():
    string = "I am happy"    
    result = make_snippet(string)
    assert result == "I am happy"

"""
Given an empty string
returns empty string
"""
def test_given_an_empty_string_returns_same_string():
    string = ""    
    result = make_snippet(string)
    assert result == ""

"""
Given words seperated by commas
Returns same words
"""
def test_given_string_seprated_by_commas_returns_same_string():
    string = "Blah,Blah,Blah,Sheep,Have,You,Any,Wool"
    result = make_snippet(string)
    assert result == "Blah,Blah,Blah,Sheep,Have,You,Any,Wool"