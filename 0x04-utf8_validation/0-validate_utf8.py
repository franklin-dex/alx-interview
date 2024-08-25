#!/usr/bin/python3
'''
method that determines if a given data set represents a valid UTF-8 encoding
'''


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
    data: List of integers, each representing a byte.

    Returns:
    True if data is a valid UTF-8 encoding, otherwise False.
    """

    '''Number of bytes in the current UTF-8 character'''
    num_bytes = 0

    '''Masks for checking the most significant bits'''
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        '''Mask to isolate the significant bits for checking byte patterns'''
        mask = 1 << 7
        if num_bytes == 0:
            '''Determine the number of bytes in the current UTF-8 character'''
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            '''1-byte characters or invalid UTF-8'''
            if num_bytes == 0:
                continue

            '''first byte must start with 2, 3, or 4 bytes long'''
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            '''Check that the current byte is a continuation byte: 10xxxxxx'''
            if not (byte & mask1 and not (byte & mask2)):
                return False

        '''Reduce the number of bytes remaining to check'''
        num_bytes -= 1

    '''If all characters are valid UTF-8, num_bytes should be zero'''
    return num_bytes == 0
