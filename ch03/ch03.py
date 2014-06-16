import re


# Problem 1.
# Refer to listfiles.py

# Problem 2.
# Refer to extcount.py

# Problem 5.
# Refer to wget.py

# Problem 6.
# Refer to antihtml.py

# Problem 7.
def make_slug(name):
    '''
    >>> make_slug("hello world")
    'hello-world'
    >>> make_slug("hello  world!")
    'hello-world'
    >>> make_slug(" --hello-  world--")
    'hello-world'
    '''
    p1 = re.compile(r'^\W+|\W+$')
    p2 = re.compile(r'\W+')
    return p2.sub('-', p1.sub('', name))

if __name__ == '__main__':
    import doctest
    doctest.testmod()


