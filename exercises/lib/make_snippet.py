"""
A function called make_snippet that takes a 
string as an argument and returns the first 
five words and then a '...' if there are more than that.
"""
def make_snippet(string):
    splitted_string = string.split()
    if len(splitted_string) <= 5:
        return (" ").join(splitted_string)
    else:
        splitted_snippet = splitted_string[:5]
        snippet = (" ").join(splitted_snippet)
        return snippet + "..."