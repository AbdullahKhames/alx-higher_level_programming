#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    val = float('-inf')
    best_key = None
    for k,v in a_dictionary.items():
        if v > val:
            val = v
            best_key = k
    return best_key
