import sys
from os.path import splitext


class IterLines(object):
    def __init__(self, file_object, line_nums):
        self.f = file_object
        self.n = line_nums

    def __iter__(self):
        return self

    def next(self):
        lines = []
        for i in range(self.n):
            line = self.f.readline()
            if not line:
                if lines:
                    return lines
                raise StopIteration()
            lines.append(line)
        return lines

def split_file(filename, num):
    num = int(num)
    with open(filename) as origin_file:
        for idx, lines in enumerate(IterLines(origin_file, num)):
            with open('%s-%d%s'%(splitext(filename)[0], idx,
                      splitext(filename)[1]), 'w') as new_file:
                new_file.write(''.join(lines))

def main():
    if len(sys.argv) != 3:
        print 'Usage: python {0} filename num'.format(sys.argv[0])
        sys.exit(1)

    split_file(*sys.argv[1:])

if __name__ == '__main__':
    main()
