def read_utf8_file(filename):
    with open(filename, 'r') as f:
        print(unicode(f.read(), 'utf-8'))


def write_utf8_file(filename):
    with open(filename, 'w') as f:
        f.write(u'\u2603 - \u2603'.encode('utf-8'))
