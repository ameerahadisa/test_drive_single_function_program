from lib.count_words import count_words
"""
When given string with one word 
Returns one
"""
def test_when_given_string_with_one_word_return_one():
    string = "House"
    result = count_words(string)
    assert result == 1

"""
When given string with two words
Returns two
"""
def test_when_given_string_with_two_words_return_two():
    string = "House mates"
    result = count_words(string)
    assert result == 2

"""
When given string with a number of words
Returns number
"""
def test_when_given_string_returns_number_of_words_in_string():
    string = "A man who thinks all the time has nothing to think about except thoughts"
    result = count_words(string)
    assert result == 14

"""
When given string with no words
Returns 0
"""
def test_when_given_empty_string_return_0():
    string = ""
    result = count_words(string)
    assert result == 0
