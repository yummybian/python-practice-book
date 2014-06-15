import operator
import string


# Problem 2.

def sum_num(lst):
    """
    >>> sum_num([1, 2, 3])
    6
    """
    return reduce(operator.add, lst)

# Problem 3.

def sum_str(lst):
    """
    >>> sum_str(["hello", "world"])
    'helloworld'
    >>> sum_str(["aa", "bb", "cc"])
    'aabbcc'
    """
    return ''.join(lst)

# Problem 4.

def product(lst):
    """
    >>> product([1, 2, 3])
    6
    """
    return reduce(operator.mul, lst, 1)

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
        res.append(sum_num(lst[:i+1]))
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
        res.append(product(lst[:i+1]))
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

# Problem 11.

def dups(lst):
    """
    >>> dups([1, 2, 1, 3, 2, 5])
    [1, 2]
    """
    return list(set(filter(lambda x: lst.count(x) != 1, lst)))

# Problem 12.

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

# Problem 13.

def lensort(lst):
    """
    >>> lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
    ['c', 'perl', 'java', 'ruby', 'python', 'haskell']
    """
    return sorted(lst, key=lambda x: len(x))

# Problem 14.

def unique_str(lst, key=lambda x:x):
    """
    >>> unique_str(['python', 'java', 'Python', 'Java'], key=lambda s: s.lower())
    ['python', 'java']
    """
    return unique(map(key, lst))

# Problem 16.

def extsort(lst):
    """
    >>> extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
    ['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']
    """
    return sorted(lst, key=lambda x: x.split('.')[1])

# Problem 17.
# Refer to reverse1.py

# Problem 18.
# Refer to reverse2.py

# Problem 19.
# Refer to head.py and tail.py

# Problem 20.
# Refer to grep.py

# Problem 21.
# Refer to wrap.py

# Problem 22.
# Refer to wordwrap.py

# Problem 24.

def zip(lst1, lst2):
    """
    >>> zip([1, 2, 3], ["a", "b", "c"])
    [(1, 'a'), (2, 'b'), (3, 'c')]
    """
    return [(lst1[i], lst2[i]) for i in range(min(len(lst1), len(lst2)))]

# Problem 25.

def square(x):
    return x * x

def map(fn, lst):
    """
    >>> map(square, range(5))
    [0, 1, 4, 9, 16]
    """
    return [fn(x) for x in lst]

# Problem 26.

def even(x): return x %2 == 0

def filter(fn, lst):
    return [x for x in lst if fn(x)]

# Problem 27.

def triplets(n):
    """
    >>> triplets(5)
    [(1, 1, 2), (1, 2, 3), (1, 3, 4), (2, 2, 4)]
    """
    return [(x, y, z) for x in range(1, n) for y in range(x, n)
            for z in range(y, n) if x+y==z]

# Problem 28.

def enumerate(lst):
    """
    >>> enumerate(["a", "b", "c"])
    [(0, 'a'), (1, 'b'), (2, 'c')]
    >>> for index, value in enumerate(["a", "b", "c"]):
    ...     print index, value
    0 a
    1 b
    2 c
    """
    return [(i, lst[i]) for i in range(len(lst))]

# Problem 29.

def array(row, col):
    """
    >>> a = array(2, 3)
    >>> a
    [[None, None, None], [None, None, None]]
    """
    return [[None for c in range(col)] for r in range(row)]


# Problem 30.
# Refer to parse_csv.py


# Problem 31.
# Refer to parse.py

# Problem 32.

def mutate(word):
    """
    >>> words = mutate('hello')
    >>> 'helo' in words
    True
    >>> 'cello' in words
    True
    >>> 'helol' in words
    True
    """
    inserting = [word[:i]+x+word[i:] for i in range(len(word))
                for x in list(string.ascii_lowercase)]
    deleting = [word[:i]+word[i+1:] for i in range(len(word))]
    replacing = [word[:i]+x+word[i+1:] for i in range(len(word))
                for x in list(string.ascii_lowercase)]
    swapping = [word[:i]+word[i+1]+word[i]+word[i+2:]
                for i in range(len(word)-1)]
    all = inserting + deleting + replacing + swapping
    return all

# Problem 33.

def nearly_equal(word1, word2):
    """
    >>> nearly_equal('python', 'perl')
    False
    >>> nearly_equal('perl', 'pearl')
    True
    >>> nearly_equal('python', 'jython')
    True
    >>> nearly_equal('man', 'woman')
    False
    """
    return True if word2 in mutate(word1) else False

# Problem 34.

def word_frequency(words):
    """Returns frequency of each word given a list of words.
    >>> word_frequency(['a', 'b', 'a'])
    {'a': 2, 'b': 1}
    """
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return dict(sorted(frequency.iteritems(), key=operator.itemgetter(1)))

# Problem 36.

def find_key(keys, word):
    for key in keys:
        if len(key) != len(word):
            continue
        elif sorted(list(key)) == sorted(list(word)):
            return key
        else:
            continue
    return None

def anagrams(lst):
    """
    >>> anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
    [['eat', 'ate', 'tea'], ['done', 'node'], ['soup']]
    """
    keys = []
    res = []
    for word in lst:
        key = find_key(keys, word)
        if key is not None:
            res[keys.index(key)].append(word)
        else:
            res.append([word])
            keys.append(word)

    return res

# Problem 37.

def valuesort(d):
    """
    >>> valuesort({'x': 1, 'y': 2, 'a': 3})
    [3, 1, 2]
    """
    return [value for key, value in sorted(d.iteritems(),
            key=operator.itemgetter(0))]

# Problem 38.

def invertdict(d):
    """
    >>> invertdict({'x': 1, 'y': 2, 'z': 3})
    {1: 'x', 2: 'y', 3: 'z'}
    """
    return dict([(value, key) for key, value in d.iteritems()])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
