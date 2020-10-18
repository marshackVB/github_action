from fuzzywuzzy import fuzz

def token_set(x, y):
    return fuzz.token_set_ratio(x, y)



    




