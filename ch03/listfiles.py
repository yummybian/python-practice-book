import sys
from os import listdir
from os.path import isfile, join


def list_files(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

def main():
    if len(sys.argv) != 2:
        print 'Usage: python {0} dir'.format(sys.argv[0])
        sys.exit(1)

    print '\n'.join(list_files(sys.argv[1]))

if __name__ == '__main__':
    main()
