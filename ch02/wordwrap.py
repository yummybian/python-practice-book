import sys


def wordwrap(filename, width):
    res = []
    def process_line(line):
        start = 0
        acc = 0
        lst = []
        step = int(width)
        for i, c in enumerate(line):


        for idx, word in enumerate(line):
            print line
            acc = acc + len(word)
            if acc < int(width):
                continue
            print idx, line[start:idx]

            lst.append(line[start:idx])
            start = idx
            acc = 0
        return lst

    with open(filename) as f:
        for line in f:
            print '-------'
            res.extend(process_line(line.split()))
    return res

def main():
    if len(sys.argv) != 3:
        print 'Usage: python {0} she.txt keyword'.format(sys.argv[0])
        sys.exit(1)

    argv = sys.argv[1:]
    print '\n'.join(wordwrap(*argv[:2]))

if __name__ == '__main__':
    main()











