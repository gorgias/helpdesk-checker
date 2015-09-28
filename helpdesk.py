import requests
from StringIO import StringIO
import csv
import sys

def main():
    w = StringIO()
    with open(sys.argv[1], 'r') as f:
        writer = csv.DictWriter(w, ['name', 'helpdesk'], dialect=csv.excel)
        for name in f.read().splitlines():
            print >>sys.stderr, "checking", name
            writer.writerow({
                'name': name,
                'helpdesk': check(name)
            })
    print w.getvalue()


def check(name):
    res = requests.get('http://%s.zendesk.com' % name)
    if res.status_code == 200:
        return 'zendesk'

    res = requests.get('http://%s.desk.com' % name)
    if res.status_code == 200 and not 'Sorry, We Couldn\'t Find That Page' in res.content:
        return 'desk'

    return ""

if __name__ == '__main__':
    main()

