import sys
import string

def process_line(line, width):
    lst = []
    i, end = 0, 0
    step = int(width)
    length = len(line)
    while i < length:
        if i+step < length:
            if line[i+step] != ' ':
                end = string.rindex(line[:i+step], ' ')
                lst.append(line[i:end])
                i = end + 1
            else:
                lst.append(line[:i])
                i = i + 1
        else:
            lst.append(line[i:].strip())
            break;

    return lst

def wordwrap(filename, width):
    res = []
    with open(filename) as f:
        for line in f:
            res.extend(process_line(line, width))
    return res

def main():
    if len(sys.argv) != 3:
        print 'Usage: python {0} she.txt width'.format(sys.argv[0])
        sys.exit(1)

    argv = sys.argv[1:]
    print '\n'.join(wordwrap(*argv[:2]))

if __name__ == '__main__':
    main()











