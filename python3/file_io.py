def read_utf8_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())


def write_utf8_file(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\u2603 - \u2603')
