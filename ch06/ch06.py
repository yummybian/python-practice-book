# Problem 1.

def product(a, b):
    """
    >>> product(3, 4)
    12
    """
    if a == 1:
        return b
    return b + product(a-1, b)

# Problem 2.

def flatten_dict(d, parent_key=None, result=None):
    '''
    >>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'z': 5, 'c': 4})
    {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
    '''
    if result is None:
        result = {}

    for key, value in d.iteritems():
        if isinstance(value, dict):
            parent_key = key
            flatten_dict(value, parent_key, result)
        else:
            if parent_key:
                print key, value
                key = '.'.join([parent_key, key])
                result[key] = value
            else:
                result[key] = value
    print '--------'
    parent_key = None

    return result


# Problem 5.
# Refer to wget.py


# Problem 7.


if __name__ == '__main__':
    import doctest
    doctest.testmod()


