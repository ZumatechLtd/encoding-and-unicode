if __name__ == "__main__":
    # String types
    print 'This is a bytestring'
    print type('This is a bytestring')
    print u'This is a unicode string'
    print type(u'This is a unicode string')

    # Examples
    print '\xe2\x98\x83'
    print u'\u2603'

    # String functions
    print hex(ord('a'))
    print chr(0x61)
    print unichr(0x2603)
