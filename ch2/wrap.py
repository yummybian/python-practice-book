import sys


def wrap(filename, width):
    res = []
    w = int(width)
    with open(filename) as f:
        for line in f:
            res.append(line.strip()[:w])
            if len(line) > w:
                res.append(line.strip()[w:])
    return res

def main():
    if len(sys.argv) != 3:
        print 'Usage: python {0} she.txt keyword'.format(sys.argv[0])
        sys.exit(1)

    argv = sys.argv[1:]
    print '\n'.join(wrap(*argv[:2]))

if __name__ == '__main__':
    main()











