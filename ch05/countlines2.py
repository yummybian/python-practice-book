import sys
import os


def count_per_file(name):
    with open(name) as f:
        return len(filter(lambda line: not line.strip() or
                   line.startswith('#'), f.readlines()))

def iter_files(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith('.py'):
                yield count_per_file(os.path.join(root, name))

def main():
    if len(sys.argv) != 2:
        print 'Usage: python {0} dir'.format(sys.argv[0])
        sys.exit(1)

    sum_lines = sum(iter_files(sys.argv[1]))
    print 'Total lines {sum}'.format(sum=sum_lines)

if __name__ == '__main__':
    main()
