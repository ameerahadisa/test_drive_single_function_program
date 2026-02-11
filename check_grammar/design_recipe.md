# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

```python
def check_grammar():
    """
    Checks that the text starts with a capital letter amd ends with a sentence ending punctuation mark ".?!"

    Parameters: 
        text: a string containing words(e.g. "This is a compter.")

    Returns: 
        a string telling user if the grammer is correct or incorrect(e.g. "Grammar is correct!", "Grammar is incorrect!")
    
    Side effects:
        This function doesn't have any side effects
    """
    pass
```

## 3. Create Examples as Tests

```python
"""
When given text starting a lowercase letter 
ending with no punctuation 
returns "Grammar is incorrect!"
"""
check_grammar("i had a great day") => "Grammar is incorrect!"

"""
When given text starting a lowercase letter 
ending with punctuation that is not sentence-ending
returns "Grammar is incorrect!"
"""
check_grammar("i had a great day|") => "Grammar is incorrect!"

"""
When given text starting a lowercase letter 
ending with correct sentence ending punctuation "."
returns "Grammar is incorrect!"
"""
check_grammar("i had a great day.") => "Grammar is incorrect!"

"""
When given text starting a lowercase letter 
ending with correct sentence ending punctuation "!"
returns "Grammar is incorrect!"
"""
check_grammar("i had a great day!") => "Grammar is incorrect!"

"""
When given text starting a lowercase letter 
ending with correct sentence ending punctuation "?"
returns "Grammar is incorrect!"
"""
check_grammar("i had a great day?") => "Grammar is incorrect!"


"""
When given text starting a uppercase letter 
ending with no punctuation 
returns "Grammar is incorrect!"
"""
check_grammar("I had a great day") => "Grammar is incorrect!"

"""
When given text starting a uppercase letter 
ending with punctuation that is not correct for
ending a sentence returns "Grammar is incorrect!"
"""
check_grammar("I had a great day/") => "Grammar is incorrect!"

"""
When given text starting a uppercase letter 
ending with correct sentence ending punctuation "."
returns "Grammar is correct!"
"""
check_grammar("I had a great day.") => "Grammar is correct!"

"""
When given text starting a uppercase letter 
ending with correct sentence ending punctuation "?"
returns "Grammar is correct!"
"""
check_grammar("What is the day today?") => "Grammar is correct!"

"""
When given text starting a uppercase letter 
ending with correct sentence ending punctuation "!"
returns "Grammar is correct!"
"""
check_grammar("I had a great day!") => "Grammar is correct!"

"""
When given a text that is not string
It returns an expectation error 
"""
check_grammar(1323232313) => Exception: "Text must be a string!"

```

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

