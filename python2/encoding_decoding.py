if __name__ == "__main__":
    print unicode('\xe2\x98\x83', 'utf-8')
    # print(unicode('\xe2\x98\x83'))  # Generates a UnicodeDecodeError
    print u'\u2603'.encode('utf-8')
