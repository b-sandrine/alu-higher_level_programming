#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Iterate through all names in the hidden_4 module
    for name in dir(hidden_4):
        # Only print names that do not start with '__'
        if not name.startswith('__'):
            print(name)
