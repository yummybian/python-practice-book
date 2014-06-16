import sys


def wrap(filename, width):
    res = []
    w = int(width)
    with open(filename) as f:
        for line in f:
            for i in range(0, len(line), w):
                if len(line) <= i+w:
                    res.append(line[i:].strip())
                    break;
                res.append(line[i:i+w])
    return res

def main():
    if len(sys.argv) != 3:
        print 'Usage: python {0} she.txt keyword'.format(sys.argv[0])
        sys.exit(1)

    argv = sys.argv[1:]
    print '\n'.join(wrap(*argv[:2]))

if __name__ == '__main__':
    main()

