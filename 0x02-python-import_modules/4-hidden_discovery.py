#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hidden
    import re
    for name in dir(hidden):
        if not re.findall("__", name):
            print(name)
