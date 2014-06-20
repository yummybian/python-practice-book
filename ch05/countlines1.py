import sys
import os


def count_lines(name):
    with open(name) as f:
        return len(f.readlines())

def iter_files(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith('.py'):
                yield os.path.join(root, name)

def main():
    sum_lines = 0
    if len(sys.argv) != 2:
        print 'Usage: python {0} dir'.format(sys.argv[0])
        sys.exit(1)

    for name in iter_files(sys.argv[1]):
        sum_lines += count_lines(name)

    print 'Total lines {sum}'.format(sum=sum_lines)

if __name__ == '__main__':
    main()
