#!/usr/bin/python3


def multiple_returns(sentence):
    length = len(sentence)
    if sentence != "":
        first_char = sentence[0]
        return length, first_char
    return length, None
