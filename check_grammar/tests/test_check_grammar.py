import pytest
from lib.check_grammar import check_grammar

"""
When given text starting a lowercase letter 
ending with no punctuation 
returns "Grammar is incorrect"
"""
def test_given_text_starts_with_lowercase_letter_and_ends_with_no_punctuation():
    text = "i had a great day"
    result = check_grammar(text)
    assert result == "Grammar is incorrect!"

"""
When given text starting a lowercase letter 
ending with punctuation that is not sentence-ending
returns "Grammar is incorrect!"
"""
def test_given_text_starts_with_lowercase_letter_and_ends_with_incorrect_punctuation():
    text = "i had a great day|"
    result = check_grammar(text)
    assert result == "Grammar is incorrect!"

"""
When given text starting a lowercase letter 
ending with correct sentence ending punctuation "."
returns "Grammar is incorrect!"
"""
def test_given_text_starts_with_lowercase_letter_and_ends_with_correct_punctuation_1():
    text = "i had a great day."
    result = check_grammar(text)
    assert result == "Grammar is incorrect!"

"""
When given text starting a lowercase letter 
ending with correct sentence ending punctuation "!"
returns "Grammar is incorrect!"
"""
def test_given_text_starts_with_lowercase_letter_and_ends_with_correct_punctuation_2():
    text = "i had a great day!"
    result = check_grammar(text)
    assert result == "Grammar is incorrect!"

"""
When given text starting a lowercase letter 
ending with correct sentence ending punctuation "?"
returns "Grammar is incorrect!"
"""
def test_given_text_starts_with_lowercase_letter_and_ends_with_correct_punctuation_3():
    text = "i had a great day?"
    result = check_grammar(text)
    assert result == "Grammar is incorrect!"

"""
When given text starting a uppercase letter 
ending with no punctuation 
returns "Grammar is incorrect!"
"""
def test_given_text_starts_with_uppercase_letter_and_ends_with_no_punctuation():
    text = "I had a great day"
    result = check_grammar(text)
    assert result == "Grammar is incorrect!"

"""
When given text starting a uppercase letter 
ending with punctuation that is not correct for
ending a sentence returns "Grammar is incorrect!"
"""
def test_given_text_starts_with_uppercase_letter_and_ends_with_incorrect_punctuation():
    text = "I had a great day/"
    result = check_grammar(text)
    assert result == "Grammar is incorrect!"

"""
When given text starting a uppercase letter 
ending with correct sentence ending punctuation "."
returns "Grammar is correct!"
"""
def test_given_text_starts_with_uppercase_letter_and_ends_with_correct_punctuation_1():
    text = "I had a great day."
    result = check_grammar(text)
    assert result == "Grammar is correct!"

"""
When given text starting a uppercase letter 
ending with correct sentence ending punctuation "?"
returns "Grammar is correct!"
"""
def test_given_text_starts_with_uppercase_letter_and_ends_with_correct_punctuation_2():
    text = "What is the day today?"
    result = check_grammar(text)
    assert result == "Grammar is correct!"

"""
When given text starting a uppercase letter 
ending with correct sentence ending punctuation "!"
returns "Grammar is correct!"
"""
def test_given_text_starts_with_uppercase_letter_and_ends_with_correct_punctuation_3():
    text = "I had a great day!"
    result = check_grammar(text)
    assert result == "Grammar is correct!"

"""
When given a text that is not string
It returns an expectation error 
"""
def test_given_text_that_is_not_string_returns_error():
    text = 1323232313
    with pytest.raises(Exception) as error:
        check_grammar(text)
    
    error_msg = str(error.value)

    assert error_msg == "Text must be a string!"
    