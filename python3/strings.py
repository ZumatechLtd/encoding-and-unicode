if __name__ == "__main__":
    print(b'This is a bytestring')
    print(type(b'This is a bytestring'))
    print('This is a unicode string')
    print(type('This is a unicode string'))

    # Examples
    print(b'\xe2\x98\x83')
    print('\u2603')

    # String functions
    print(hex(ord('a')))
    print(hex(ord(b'a')))
    print(hex(ord('\u2603')))
    print(chr(0x2603))
