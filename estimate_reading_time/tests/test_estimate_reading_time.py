import pytest
from lib.estimate_reading_time import estimate_reading_time
"""
When given an empty text
It returns a reading time of 0
"""
def test_given_text_with_no_words_returns_0():
    text = ""
    result = estimate_reading_time(text)
    assert result == 0

"""
When given a text with one word
It returns a reading time of 0.005 minute(s)
"""
def test_given_a_text_with_one_word_returns_0_005():
    text = "hello "
    result = estimate_reading_time(text)
    assert result == 0.005

"""
When given a text with two words
It returns a reading time of 0.01 minute(s)
"""
def test_given_text_with_2_words_returns_0_01():
    text = "hello world"
    result = estimate_reading_time(text)
    assert result == 0.01

"""
When given a text with 200 words
It returns a reading time of 1 minute(s)
"""
def test_given_text_with_200_words_returns_1():
    text = "hello world " * 100
    result = estimate_reading_time(text)
    assert result == 1

"""
When given a text with 201 words
It returns a reading time of 1.005 minute(s)
"""
def test_given_text_with_201_words_returns_1_005():
    text = "hello " * 201
    result = estimate_reading_time(text)
    assert result == 1.005

"""
When given a text with 300 words
It returns a reading time of 1.5 minute(s)
"""
def test_given_text_with_300_words_returns_1_5():
    text = "hello " * 300
    result = estimate_reading_time(text)
    assert result == 1.5

"""
When given a text with 424 words
It returns a reading time of 2.12 minute(s)
"""
def test_given_text_with_300_words_returns_2_12():
    text = "hello " * 424
    result = estimate_reading_time(text)
    assert result == 2.12

"""
When given a text with 500 words
It returns a reading time of 2.5 minute(s)
"""
def test_given_text_with_500_words_returns_2_5():
    text = "hello " * 500
    result = estimate_reading_time(text)
    assert result == 2.5

"""
When given a text with 50000 words
It returns a reading time of 250 minute(s)
"""
def test_given_text_with_50000_words_returns_250():
    text = "hello " * 50000
    result = estimate_reading_time(text)
    assert result == 250

"""
When given a text with 38844 words
It returns a reading time of 194.22 minute(s)
"""
def test_given_text_with_38844_words_returns_194_22():
    text = "hello " * 38844
    result = estimate_reading_time(text)
    assert result == 194.22

"""
When given a text that is not string
It returns an expectation error 
"""
def test_given_text_that_is_not_string_returns_error():
    text = 5003
    with pytest.raises(Exception) as error:
        estimate_reading_time(text)
    
    error_msg = str(error.value)

    assert error_msg == "Text must be a string"
    