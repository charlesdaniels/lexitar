#!/usr/bin/env python3

import os
import sys
import argparse
import dictionary
import textwrap
import reedsolo
import bz2
import re
import string

chunksize = 16
stream_version = 1

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--encode", "-e", default=None,
                        help="Encode the specified file and print to stdout.")
    parser.add_argument("--decode", "-c", default=None,
                        help="Decode the specified file and write to stdout.")

    args = parser.parse_args()

def pack_stream(data, nsym):
    """pack_stream

    Pack the specified data into the Lexitar stream format and return it.

    The data is bz2 encoded, then the reed-solomon encoding for it is
    calculated, finally it is padded with null bytes until the packed stream
    length is a multiple of chunksize / 8 bytes.

    The result is returned.

    :param data:
    """

    data = bytes(data)
    #  data = bz2.compress(data)

    rs = reedsolo.RSCodec(nsym)
    data = rs.encode(data)

    while len(data) % int(chunksize / 8) != 0:
        data += bytes([0])

    return data

def unpack_stream(data):
    """unpack_stream

    Inverse pack_stream()

    :param data:
    """

    rs = reedsolo.RSCodec()
    data = rs.decode(data)
    #  data = bz2.decompress(data)

    return data


def encode_translate(data):
    """encode_translate

    Encode bytes by replacing them with the chunks in the dictionary.

    :param data:
    """

    encoded = ""
    idx = 0
    while idx < len(data):
        chunk = data[idx:idx + int(chunksize / 8)]
        if chunk == b'':
            continue

        idx += int(chunksize / 8)
        encoded += " "
        encoded += dictionary.by_chunk[bytes(chunk)]

    return encoded

def encode(data, linelength=72, nsym = 20):
    """encode

    Encode the specified data, and return it as a string. it is automatically
    wrapped to the specified line length.

    :param data: The data to encode, must be cast-able to bytes()
    :param linelength: Desired line length for return
    """
    data = pack_stream(data, nsym)
    encoded = '\n'.join(textwrap.wrap(encode_translate(data), linelength))
    return encoded

def decode_translate(data):
    """decode_translate

    Return the bytes encoded by the given string.

    :param data:
    """
    result = bytes()
    for coding in data.split():
        if coding not in dictionary.by_coding:
            # ignore anything unknown
            sys.stderr.write("WARNING: '{}' not a known coding.\n"
                            .format(coding))
            continue

        result = result + dictionary.by_coding[coding]

    return result


def decode(data):
    """decode

    Decode the given string and return the resulting bytes.

    :param data: string with message to decode
    """

    data = str(data)
    data = data.strip()
    data = data.lower()

    # collapse whitespace
    r = re.compile(r'\W+')
    r.sub(' ', data)

    # remove punctuation
    r = re.compile(r'[^\W\s]')
    r.sub('', data)

    result = decode_translate(data)
    result = unpack_stream(result)
    return result


if __name__ == "__main__":
    main()

