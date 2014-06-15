import sys


def grep(filename, keyword):
    with open(filename) as f:
        return filter(lambda line: keyword in line, f.readlines())

def main():
    if len(sys.argv) != 3:
        print 'Usage: python {0} she.txt keyword'.format(sys.argv[0])
        sys.exit(1)

    argv = sys.argv[1:]
    print ''.join(grep(*argv[:2])).strip()

if __name__ == '__main__':
    main()











