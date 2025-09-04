#!/usr/bin/python3
""" This is module
"""


def text_indentation(text=None):
    """ Function that prints a text with 2 new lines
        after each of these characters: ., ? and :

    Args:
        text (str, optional): Text to be traited. Defaults to None.

    Raises:
        TypeError: Raises when the text is not an actual string
    """
    if type(text) is not str or text is None:
        raise TypeError("text must be a string")
    output = ""
    line = ""
    for ch in text:
        line += ch
        if ch in ['.', ':', '?']:
            output += "{}\n\n".format(line.strip())
            line = ""
            continue
    output += "{}".format(line.strip())
    print(output, end="")
    