import re

def findWords(text):
    words = []
    pattern = '([^A-z]|^)(?P<cubifyString>[A-z]( [A-z]){4,40})([^A-z]|$)'
    for m in re.finditer(pattern, text, re.I):
        cubifyString = m.group('cubifyString')
        words.append(cubifyString)
    return words