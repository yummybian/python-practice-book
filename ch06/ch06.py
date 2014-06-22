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

# Problem 4.

def treemap(fn, lst, result=None):
    '''
    >>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
    [1, 4, [9, 16, [25]]]
    '''
    if result is None:
        result = []

    for x in lst:
        if isinstance(x, list):
            result.append(treemap(fn, x, None))
        else:
            result.append(fn(x))

    return result

# Problem 5.

def tree_reverse(lst, result=None):
    '''
    >>> tree_reverse([[1, 2], [3, [4, 5]], 6])
    [6, [[5, 4], 3], [2, 1]]
    '''
    if result is None:
        result = []

    for x in lst:
        if isinstance(x, list):
            result.insert(0, tree_reverse(x, None))
        else:
            result.insert(0, x)

    return result

# Problem 6.

def json_encode(data):
    if isinstance(data, bool):
        if data:
            return "true"
        else:
            return "false"
    elif isinstance(data, (int, float)):
        return str(data)
    elif isinstance(data, str):
        return '"' + escape_string(data) + '"'
    elif isinstance(data, (tuple, list)):
        return "[" + ", ".join(json_encode(d) for d in data) + "]"
    elif isinstance(data, dict):
        return "{" + ", ".join('{key}:{value}'.format(key=json_encode(k), value=json_encode(v))
                for k, v in data.iteritems()) + "}"
    else:
        raise TypeError("%s is not JSON serializable" % repr(data))

def escape_string(s):
    """Escapes double-quote, tab and new line characters in a string."""
    s = s.replace('"', '\\"')
    s = s.replace("\t", "\\t")
    s = s.replace("\n", "\\n")
    return s


if __name__ == '__main__':
    import doctest
    doctest.testmod()


