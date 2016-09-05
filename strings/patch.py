#!/usr/bin/env python3
import sys, os

def usage():
    print("{} <binary> <offset> <new string>".format(sys.argv[0]))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage()
        exit(-1)

    binary = sys.argv[1]
    offset = int(sys.argv[2], 0) # Supports hex by putting "0x" in front.
    string = sys.argv[3]

    if not os.path.exists(binary):
        print("Binary '{}' doesn't exist! Aborting..".format(binary))
        exit(-1)

    slen = len(string)
    print("Patching \"{}\" at offset {} with: \"{}\" ({} bytes)"
          .format(binary, offset, string, slen))

    f = open(binary, mode = "rb")
    data = bytearray(f.read())
    f.close()
    print("Read {} bytes".format(len(data)))

    if offset > len(data):
        print("Offset {} is not inside binary! Aborting..".format(offset))
        exit(-1)

    size = 0
    for i in range(offset, len(data)):
        if data[i] == 0:
            break
        size += 1
    print("Size of string at {} is {} bytes".format(offset, size))

    if slen > size:
        print("Input string size {} > {} bytes! Aborting..".format(slen, size))
        exit(-1)

    print("Changing values at {} to {}".format(offset, offset + slen))
    for i in range(len(string)):
        data[offset + i] = ord(string[i])

    print("Writing new data")
    f = open(binary, mode = "wb")
    f.write(data)
    f.close()
