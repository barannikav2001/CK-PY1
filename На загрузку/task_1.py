# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

def get_dict(a):
    return{"bin":bin(a), "dec": a,"hex":hex(a), "oct": oct(a)}

pprint([get_dict(b) for b in range(16)])