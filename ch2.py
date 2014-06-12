import operator


# Problem 2.

def sum_num(lst):
    """
    >>> sum_num([1, 2, 3])
    4
    """
    return reduce(operaor.add, lst)

# Problem 3.

def sum_str(lst):
    """
    >>> sum_str(["hello", "world"])
    "helloworld"
    >>> sum_str(["aa", "bb", "cc"])
    "aabbcc"
    """
    return ''.join(lst)

# Problem 4.

def product(lst):
    """
    >>> product([1, 2, 3])
    6
    """
    return reduce(operator.mul, lst)

# Problem 5.

def factorial(num):
    """
    >>> factorial(4)
    24
    """
    return product(map(lambda x: x+1, range(4)))

# Problem 6.

def reverse(lst):
    """
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverse(reverse([1, 2, 3, 4]))
    [1, 2, 3, 4]
    """
    return lst[::-1]

# Problem 8.

def cumulative_sum(lst):
    """
    >>> cumulative_sum([1, 2, 3, 4])
    [1, 3, 6, 10]
    >>> cumulative_sum([4, 3, 2, 1])
    [4, 7, 9, 10]
    """
    res = []
    for i in xrange(len(lst)):
        res[i] = sum_num(lst[:i+1])
    return res

# Problem 9.

def cumulative_product(lst):
    """
    >>> cumulative_product([1, 2, 3, 4])
    [1, 2, 6, 24]
    >>> cumulative_product([4, 3, 2, 1])
    [4, 12, 24, 24]
    """
    res = []
    for i in xrange(len(lst)):
        res[i] = product(lst[:i+1])
    return res

# Problem 10.

def unique(lst):
    """
    >>> unique([1, 2, 1, 3, 2, 5])
    [1, 2, 3, 5]
    """
    return list(set(lst))

def unique_rec(lst):
    """
    >>> unique_rec([1, 2, 1, 3, 2, 5])
    [1, 2, 3, 5]
    """
    if len(lst) == 1:
        return lst
    elif lst[-1] in lst[0:-1]:
        return unique_rec(lst[0:-1])
    else:
        return unique_rec(lst[0:-1]) + [lst[-1]]

# problem 11.

def dups(lst):
    """
    >>> dups([1, 2, 1, 3, 2, 5])
    [1, 2]
    """
    pass


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

def unique_str(lst, key=lambda x:x):
    """
    >>> unique_str(['python', 'java', 'Python', 'Java'], key=lambda s: s.lower())
    ['python', 'java']
    """
    return unique(map(key, lst))

def extsort(lst):
    """
    >>> extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
    ['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']
    """
    return sorted(lst, key=lambda x: x.split('.')[1])

if __name__ == '__main__':
    import doctest
    doctest.testmod()

