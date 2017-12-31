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

def encode_header(length):
    """encode_header

    The header has the following format:

    byte 0-3 : magic string 'lxt'
    byte 4   : stream version
    byte 5-7 : message length in bytes, not including padding

    :param length:
    """

    length = int(length)
    header = b''
    magic = b'lxt'
    sv = stream_version.to_bytes(1, byteorder='big')
    length = length.to_bytes(4, byteorder="big")
    header = magic + sv + length

    assert(len(header) == 8)

    rs = reedsolo.RSCodec(len(header))
    header = rs.encode(header)
    return header

def decode_header(header):
    """decode_hader

    Extract length from header and return.

    :param header:
    """

    header = bytes(header)
    assert len(header) == 16

    rs = reedsolo.RSCodec(int(len(header) / 2))

    header = rs.decode(header)
    assert len(header) == 8

    magic  = (header[0:3])
    sv     = (header[3])
    length = (header[4:8])

    if magic != b'lxt':
        raise ValueError("Magic was '{}', expected '{}'"
                         .format(magic, b'lxtr'))

    if sv != stream_version:
        raise ValueError("Don't know how to decode stream version '{}'"
                         .format(sv))

    return int.from_bytes(length, byteorder="big")

def pack_stream(data, nsym):
    """pack_stream

    Pack the specified data into the Lexitar stream format and return it.

    The data is bz2 encoded, then the reed-solomon encoding for it is
    calculated, finally it is padded with null bytes until the packed stream
    length is a multiple of chunksize / 8 bytes.

    The header is appended and prepended to the data.

    The result is returned.

    :param data:
    """

    data = bytes(data)
    #  data = bz2.compress(data)

    rs = reedsolo.RSCodec(nsym)
    length = len(data)
    data = rs.encode(data)
    while len(data) % int(chunksize / 8) != 0:
        data = data + b'\x00'
    header = encode_header(length)
    data = header + data + header

    return data

def unpack_stream(data):
    """unpack_stream

    Inverse pack_stream()

    :param data:
    """

    header_1 = data[0:16]
    header_2 = data[-16:]

    assert(len(header_1) == 16)
    assert(len(header_2) == 16)

    length = None
    try:
        length = decode_header(header_1)
    except Exception as e:
        sys.stderr.write("WARNING: encountered exception while decoding" +
                         " header: '{}', attempting to".format(e) +
                         " decode backup header...\n")
        try:
            length = decode_header(header_2)
        except Exception as e:
            sys.stderr.write("FATAL: encountered exception while " +
                             "decoding backup header: '{}'".format(e) +
                             ". Both headers are corrupt!\n")
            sys.stderr.write("DEBUG: header_1: '{}'\n".format(header_1))
            sys.stderr.write("DEBUG: header_2: '{}'\n".format(header_2))
            raise ValueError("Corrupted header")

    assert(length is not None)

    data = bytearray(data[16:-16])
    rs = reedsolo.RSCodec()
    data = rs.decode(data)
    data = data[0:length]
    #  data = bz2.decompress(data)
    data = bytes(data)

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

