import sys
from os import listdir
from os.path import isfile, join


def ext_count(path):
    ext = {}
    files = (f for f in listdir(path) if isfile(join(path, f)))
    for f in files:
        s = f.split('.')[-1]
        ext[s] = ext.get(s, 0) + 1
    return ext

def main():
    if len(sys.argv) != 2:
        print 'Usage: python {0} dir'.format(sys.argv[0])
        sys.exit(1)

    ext = ext_count(sys.argv[1])
    for suff, cnt in ext.iteritems():
        print cnt, suff

if __name__ == '__main__':
    main()
