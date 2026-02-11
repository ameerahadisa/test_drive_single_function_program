# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

```python
def estimate_reading_time():
    """
    Estimates the reading time from a text assuming they can read 200 words by minutes
    The words seperated by spaces are counted

    Parameters: 
        text: a string containing words(e.g. "Text Text Text Text Text Text Text Text Text Text Text Text")

    Returns: 
        a number representing the estimated time for the text
    
    Side effects:
        This function doesn't have any side effects
    """

    pass
```

## 3. Create Examples as Tests

```python
"""
When given an empty text
It returns a reading time of 0
"""
estimate_reading_time("") => 0

"""
When given a text with one word
It returns a reading time of 0.005 minute(s)
"""
estimate_reading_time("hello") => 0.005

"""
When given a text with two words
It returns a reading time of 0.01 minute(s)
"""
estimate_reading_time("hello world") => 0.01

"""
When given a text with 200 words
It returns a reading time of 1 minute(s)
"""
estimate_reading_time("...200...") => 1

"""
When given a text with 201 words
It returns a reading time of 1.005 minute(s)
"""
estimate_reading_time("...201...") => 1.005

"""
When given a text with 300 words
It returns a reading time of 1.5 minute(s)
"""
estimate_reading_time("...300...") => 1.5

"""
When given a text with 424 words
It returns a reading time of 2.12 minute(s)
"""
estimate_reading_time("...424...") => 2.12

"""
When given a text with 500 words
It returns a reading time of 2.5 minute(s)
"""
estimate_reading_time("...500...") => 2.5


"""
When given a text with 50000 words
It returns a reading time of 250 minute(s)
"""
estimate_reading_time("...50000...") => 250

"""
When given a text with 38844 words
It returns a reading time of 194.22 minute(s)
"""
estimate_reading_time("...38844...") => 194.22


"""
When given a text that is not string
It returns an expectation error 
"""
estimate_reading_time(5003) => Exception: "Text must be a string"


```

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

