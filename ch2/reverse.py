import sys


def reverse(filename):
    with open(filename) as f:
        return f.readlines()[::-1]

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    print ''.join(reverse(argv[0])).strip()
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)

