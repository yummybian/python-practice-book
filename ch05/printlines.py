import sys

def print_lines(name, width):
    with open(name) as f:
        return [line for line in f if len(line) > width]


def main():
    if len(sys.argv) != 2:
        print 'Usage: python {0} filename'.format(sys.argv[0])
        sys.exit(1)

    for line in print_lines(sys.argv[1], 40):
        print line,


if __name__ == '__main__':
    main()
