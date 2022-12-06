#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != '':
        f_c = sentence[0]
    else:
        f_c = None
    return (len(sentence), f_c)
