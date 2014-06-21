# Problem 1.

def reverse_iter(lst):
    """
    >>> it = reverse_iter([1, 2, 3, 4])
    >>> it.next()
    4
    >>> it.next()
    3
    >>> it.next()
    2
    >>> it.next()
    1
    >>> it.next()
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    StopIteration
    """
    for x in reversed(lst):
        yield x
    raise StopIteration()


# Problem 2.
# Refer to


# Problem 5.
# Refer to wget.py


# Problem 7.


# Problem 8.

def peep(it):
    '''
    >>> it = iter(range(5))
    >>> x, it1 = peep(it)
    >>> print x, list(it1)
    0 [0, 1, 2, 3, 4]
    '''
    lst = list(it)
    first = lst[0]
    return first, iter(lst)

# Problem 9.

def my_enumerate(seq, start=0):
    '''
    >>> list(my_enumerate(["a", "b", "c"]))
    [(0, 'a'), (1, 'b'), (2, 'c')]
    >>> for i, c in my_enumerate(["a", "b", "c"]):
    ...     print i, c
    ...
    0 a
    1 b
    2 c
    '''
    n = start
    for elem in seq:
        yield n, elem
        n += 1

# Problem 10.

def my_izip(*iterables):
    '''
    >>> for x, y in my_izip(["a", "b", "c"], [1, 2, 3]):
    ...     print x, y
    ...
    a 1
    b 2
    c 3
    '''
    iterators = map(iter, iterables)
    while iterators:
        yield tuple(map(next, iterators))


if __name__ == '__main__':
    import doctest
    doctest.testmod()


