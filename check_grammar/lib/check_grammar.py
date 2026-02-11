def check_grammar(text):
    if not isinstance(text, str):
        raise Exception("Text must be a string!")
    
    first_letter = text[0]
    last_char = text[-1]
    punctuation = ".!?"

    if first_letter.isupper() and last_char in punctuation:
        return "Grammar is correct!"
    else:
        return "Grammar is incorrect!"
