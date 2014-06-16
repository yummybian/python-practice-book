import sys
from os.path import basename
from urllib2 import Request, urlopen, URLError


def wget(url):
    req = Request(url)
    try:
        response = urlopen(req)
    except URLError as e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
    else:
        name = basename(url)
        if not name:
            name = 'index.html'
        print "saving {url} as {name}".format(url=url, name=name)
        with open(name, 'w') as f:
            f.write(response.read())

def main():
    if len(sys.argv) != 2:
        print 'Usage: python {0} url'.format(sys.argv[0])
        sys.exit(1)

    wget(sys.argv[1])

if __name__ == '__main__':
    main()
