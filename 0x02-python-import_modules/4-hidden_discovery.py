#!/usr/bin/python3
if __name__ == "__main__":
    __import__("hidden_4.pyc")
    module_names = dir(hidden_4)
    for name in sorted(module_names):
        if not name.starteswith('__'):
            print(name)
