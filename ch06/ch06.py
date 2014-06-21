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
    if result is None:
        result = {}

    for key, value in d.iteritems():
        if isinstance(value, dict):
            parent_key = key
            flatten_dict(value, parent_key, result)
            parent_key = None
        else:
            if parent_key:
                key = '.'.join([parent_key, key])
                result[key] = value
            else:
                result[key] = value

    return result


# Problem 5.
# Refer to wget.py


# Problem 7.


if __name__ == '__main__':
    import doctest
    doctest.testmod()


