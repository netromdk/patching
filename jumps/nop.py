#!/usr/bin/env python3
import sys, os

def usage():
    print("{} <binary> <offset> <count>".format(sys.argv[0]))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage()
        exit(-1)

    binary = sys.argv[1]
    offset = int(sys.argv[2], 0) # Supports hex by putting "0x" in front.
    count = int(sys.argv[3])

    if not os.path.exists(binary):
        print("Binary '{}' doesn't exist! Aborting..".format(binary))
        exit(-1)

    print("Patching \"{}\" at offset {} with {} NOPs".format(binary, offset, count))

    f = open(binary, mode = "rb")
    data = bytearray(f.read())
    f.close()
    print("Read {} bytes".format(len(data)))

    if offset > len(data):
        print("Offset {} is not inside binary! Aborting..".format(offset))
        exit(-1)

    if offset + count > len(data):
        print("{} NOPs from {} is not inside binary! Aborting..".format(count, offset))
        exit(-1)

    print("Changing values at {} to {}".format(offset, offset + count))
    for i in range(count):
        data[offset + i] = 0x90

    print("Writing new data")
    f = open(binary, mode = "wb")
    f.write(data)
    f.close()
