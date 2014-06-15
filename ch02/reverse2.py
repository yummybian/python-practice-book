import sys


def reverse(filename):
    with open(filename) as f:
        return map(lambda line: line.strip()[::-1], f.readlines())

def main():
    if len(sys.argv) != 2:
        print 'Usage: python {0} she.txt'.format(sys.argv[0])
        sys.exit(1)

    argv = sys.argv[1:]
    print '\n'.join(reverse(argv[0]))

if __name__ == '__main__':
    main()



