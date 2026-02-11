def estimate_reading_time(text):
    if not isinstance(text, str):
        raise Exception("Text must be a string")
    else:
        splitted_text = text.split()
        no_of_words = len(splitted_text)
        estimated_time = no_of_words / 200
        return estimated_time