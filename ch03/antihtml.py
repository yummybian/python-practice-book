import sys
import re


def stripe_tags(name):
    with open(name) as f:
        p = re.compile(r'<.*?>')
        return p.sub('', f.read())

def main():
    if len(sys.argv) != 2:
        print 'Usage: python {0} dir'.format(sys.argv[0])
        sys.exit(1)

    print stripe_tags(sys.argv[1])

if __name__ == '__main__':
    main()
