def group(lst, size):
    """
    >>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
    [[1, 2, 3, 4], [5, 6, 7, 8], [9]]
    """
    new = []
    for i in range(0, len(lst), size):
        new.append(lst[i:i+size])
    return new

def unique1(lst):
    """
    >>> unique1([1, 2, 1, 3, 2, 5])
    [1, 2, 3, 5]
    """
    if len(lst) == 1:
        return lst
    elif lst[-1] in lst[0:-1]:
        return unique1(lst[0:-1])
    else:
        return unique1(lst[0:-1]) + [lst[-1]]

def unique2(lst, key=lambda x:x):
    """
    >>> unique2(['python', 'java', 'Python', 'Java'], key=lambda s: s.lower())
    ['python', 'java']
    """
    return unique1(map(key, lst))

def unique3(lst):
    """
    >>> unique3([1, 2, 1, 3, 2, 5])
    [1, 2, 3, 5]
    """
    return list(set(lst))

def extsort(lst):
    """
    >>> extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
    ['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']
    """
    return sorted(lst, key=lambda x: x.split('.')[1])

if __name__ == '__main__':
    import doctest
    doctest.testmod()

