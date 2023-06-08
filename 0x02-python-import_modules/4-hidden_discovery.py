#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    attributes = dir(hidden_4)
    for att in attributes:
        if  (not att.startswith("__")):
                print(att)
