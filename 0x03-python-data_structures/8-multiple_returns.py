#!/usr/bin/python3


def multiple_returns(sentence):
    """Returns the length of a string and its first character."""
    return (0, None) if sentence == "" else (len(sentence), sentence[0])