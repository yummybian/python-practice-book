import sys
import os


def count_files(path):
    cnt = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith('.py'):
                cnt += 1
    return cnt

def main():
    if len(sys.argv) != 2:
        print 'Usage: python {0} dir'.format(sys.argv[0])
        sys.exit(1)

    print count_files(sys.argv[1])

if __name__ == '__main__':
    main()
