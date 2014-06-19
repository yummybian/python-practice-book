

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


if __name__ == '__main__':
    import doctest
    doctest.testmod()


