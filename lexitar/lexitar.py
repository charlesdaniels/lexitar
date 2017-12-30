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


def encode_header(nsym):
    header = b''
    nsym = nsym.to_bytes(8, byteorder='big')
    magic = b'lexitar '
    sv = stream_version.to_bytes(2, byteorder='big')
    reserved = bytes(14)
    header = nsym + magic + sv + reserved

    assert(len(header) == 32)

    rs = reedsolo.RSCodec(len(header))
    header = rs.encode(header)
    return header

def decode_header(header):
    """decode_hader

    Extract nsym from header and return.

    :param header:
    """

    header = bytes(header)
    assert len(header) == 64

    rs = reedsolo.RSCodec(int(len(header) / 2))

    header = rs.decode(header)
    assert len(header) == 32

    nsym     = header[0:8]
    magic    = header[8:16]
    sv       = header[16:18]
    reserved = header[18:32]

    assert(magic == b'lexitar ')
    assert(sv == stream_version.to_bytes(2, byteorder='big'))
    return int.from_bytes(nsym, byteorder="big")


def pack_stream(data, correction_rate):
    """pack_stream

    Pack the specified data into the Lexitar stream format and return it.

    The data is bz2 encoded, then the reed-solomon encoding for it is
    calculated, finally it is padded with null bytes until the packed stream
    length is a multiple of chunksize / 8 bytes.

    The header is 64 bytes long and has this format:

    * bytes 0-7 specifies the nsym for the RS encoding
    * bytes 8-15 contains the magic string 'lexitar '
    * bytes 16-17 contain the stream version
    * bytes 18-31 are reserved for future use
    * bytes 31-63 are the correction symbols for the first 32 bytes, using
      reed solomon coding with nsym=32

    The header is prepended to the front of the data, and appended to the end.

    The result is returned.

    :param data:
    """

    data = bytes(data)
    data = bz2.compress(data)


    nsym = int(len(data) * correction_rate) + 1

    header = encode_header(nsym)

    rs = reedsolo.RSCodec(nsym)
    #  data = rs.encode(data)

    while len(data) % int(chunksize / 8) != 0:
        data += bytes([0])

    data = header + data + header
    return data

def unpack_stream(data):
    """unpack_stream

    Inverse pack_stream()

    :param data:
    """

    header_1 = data[0:64]
    header_2 = data[-64:]

    nsym = None
    try:
        nsym = decode_header(header_1)
    except Exception as e:
        sys.stderr.write("WARNING: encountered exception while decoding" +
                         " header: '{}', attempting to".format(e) +
                         " decode backup header...\n")
        try:
            nsym = decode_header(header_2)
        except Exception as e:
            sys.stderr.write("FATAL: encountered exception while " +
                             "decoding backup header: '{}'".format(e) +
                             ". Both headers are corrupt!\n")
            sys.stderr.write("DEBUG: header_1: '{}'\n".format(header_1))
            sys.stderr.write("DEBUG: header_2: '{}'\n".format(header_2))
            raise ValueError("Corrupted header")

    assert(nsym is not None)

    rs = reedsolo.RSCodec(1)

    data = data[64:-64]
    #  data = rs.decode(data)
    data = bz2.decompress(data)

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

def encode(data, linelength=72, correction_rate = 0.1):
    """encode

    Encode the specified data, and return it as a string. it is automatically
    wrapped to the specified line length.

    :param data: The data to encode, must be cast-able to bytes()
    :param linelength: Desired line length for return
    """
    data = pack_stream(data, correction_rate)
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

