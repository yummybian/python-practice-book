import time


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
        return "{" + ", ".join('{key}:{value}'.format(key=json_encode(k),
            value=json_encode(v)) for k, v in data.iteritems()) + "}"
    else:
        raise TypeError("%s is not JSON serializable" % repr(data))

def escape_string(s):
    """Escapes double-quote, tab and new line characters in a string."""
    s = s.replace('"', '\\"')
    s = s.replace("\t", "\\t")
    s = s.replace("\n", "\\n")
    return s

# Problem 8.

def count_change(n, lst):
    '''
    >>> count_change(10, [1, 5])
    3
    >>> count_change(10, [1, 2])
    6
    >>> count_change(100, [1, 5, 10, 25, 50])
    292
    '''
    if n == 0:
        return 1
    if n < 0 or len(lst) == 0:
        return 0
    return count_change(n, lst[1:]) + count_change(n-lst[0], lst)

# Problem 9.

def permute(lst):
    '''
    >>> permute([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    '''
    def iter_permute(lst):
        if len(lst) == 0:
            yield []

        for i in range(len(lst)):
            for cc in permute(lst[:i]+lst[i+1:]):
                yield [lst[i]] + cc

    return list(iter_permute(lst))

# Problem 10.

def profile(f):
    def g(*args, **kwargs):
        start_time = time.time()
        f(*args, **kwargs)
        print "Time taken: {consumed}".format(consumed=time.time()-start_time)

    return g

# Problem 11.

def square(x): return x * x

def vectorize(f):
    '''
    >>> f = vectorize(square)
    >>> f([1, 2, 3])
    [1, 4, 9]
    >>> g = vectorize(len)
    >>> g(["hello", "world"])
    [5, 5]
    >>> g([[1, 2], [2, 3, 4]])
    [2, 3]
    '''
    def g(lst):
        res = []
        for x in lst:
            res.append(f(x))
        return res

    return g


if __name__ == '__main__':
    import doctest
    doctest.testmod()


