import sys
import os


def find_files(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            yield os.path.join(root, name)

def main():
    if len(sys.argv) != 2:
        print 'Usage: python {0} dir'.format(sys.argv[0])
        sys.exit(1)

    for f in find_files(sys.argv[1]):
        print f

if __name__ == '__main__':
    main()
