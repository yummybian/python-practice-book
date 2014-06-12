import sys


def tail(filename):
    with open(filename) as f:
        return f.readlines()[-10:]

def main():
    if len(sys.argv) != 2:
        print 'Usage: python {0} she.txt'.format(sys.argv[0])
        sys.exit(1)

    argv = sys.argv[1:]
    print ''.join(tail(argv[0])).strip()

if __name__ == '__main__':
    main()











