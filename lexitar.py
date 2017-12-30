#!/usr/bin/env python3

import os
import sys
import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--dictionary", "-d", default="./dictionary.txt",
                        help="Path to dictioanry file." +
                        " (default: ./dictionary.txt)")
    parser.add_argument("--encode", "-e", default=None,
                        help="Encode the specified file and print to stdout.")
    parser.add_argument("--decode", "-c", default=None,
                        help="Decode the specified file and write to stdout.")

    args = parser.parse_args()

    if args.encode is not None:
        with open(args.dictionary, 'r') as d:
            with open(args.encode, 'rb') as f:
                encode(f.read(), d.readlines(), 16)
        exit()
    elif args.decode is not None:
        with open(args.dictionary, 'r') as d:
            with open(args.decode, 'r') as f:
                decode(f.readlines(), d.readlines(), 16)

def encode(data, dictionary, chunksize):
    data = bytes(data)
    dict_length = pow(2, chunksize)

    sys.stderr.write("chunksize: {}\n".format(chunksize))
    sys.stderr.write("dict_length: {}\n".format(dict_length))
    sys.stderr.write("dictionary length: {}\n".format(len(dictionary)))

    assert(len(dictionary) == dict_length)

    dictionary_table = {}
    coding = 0
    for symbol in dictionary:
        dictionary_table[coding] = symbol.strip()
        coding += 1
    dictionary = dictionary_table

    # due to the limits of bit-level manipulation in Python, the chunksize must
    # be a multiple of 8 bits.
    assert(chunksize % 8 == 0)
    chunksize = int(chunksize / 8)
    assert(len(data) % chunksize == 0)

    idx = 0
    while True:
        chunk = bytes(data[idx:idx+chunksize])
        sys.stdout.write(dictionary[int.from_bytes(chunk, "big")].strip())
        sys.stdout.write(" ")

        idx += chunksize
        if (idx + chunksize) > len(data):
            break

    sys.stdout.flush()


def decode(data, dictionary, chunksize):
    dict_length = pow(2, chunksize)

    sys.stderr.write("chunksize: {}\n".format(chunksize))
    sys.stderr.write("dict_length: {}\n".format(dict_length))
    sys.stderr.write("dictionary length: {}\n".format(len(dictionary)))

    assert(len(dictionary) == dict_length)

    # due to the limits of bit-level manipulation in Python, the chunksize must
    # be a multiple of 8 bits.
    assert(chunksize % 8 == 0)
    chunksize = int(chunksize / 8)

    dictionary_table = {}
    coding = 0
    sys.stderr.write("generating symbol table...\n")
    for symbol in dictionary:
        coding = int(coding)
        current_coding = (coding).to_bytes(chunksize, byteorder="big")
        dictionary_table[symbol.strip()] = current_coding
        #  sys.stderr.write("table[{}] = {}\n".format(symbol.strip(), current_coding))
        coding += 1
    dictionary = dictionary_table

    sys.stderr.write("decoding data...\n")
    for line in data:
        #  sys.stderr.write("processing line {}\n".format(line))
        for word in line.split():
            word = word.strip().lower()
            if word not in dictionary:
                continue
            sys.stdout.buffer.write(dictionary[word])
            #  sys.stderr.write("decoded {} to {}\n".format(word, dictionary[word]))

    sys.stdout.flush()


if __name__ == "__main__":
    main()

