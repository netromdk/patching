#!/usr/bin/env python3
import sys, os

def usage():
    print("{} <binary> <offset> [<byte>, ..]".format(sys.argv[0]))

if __name__ == "__main__":
    if len(sys.argv) < 4:
        usage()
        exit(-1)

    binary = sys.argv[1]
    offset = int(sys.argv[2], 0) # Supports hex by putting "0x" in front.

    values = []
    for byte in sys.argv[3:]:
        values.append(int(byte, 0))

    if not os.path.exists(binary):
        print("Binary '{}' doesn't exist! Aborting..".format(binary))
        exit(-1)

    print("Patching \"{}\" at offset {} with: {} ({} bytes)"
          .format(binary, offset, values, len(values)))

    f = open(binary, mode = "rb")
    data = bytearray(f.read())
    f.close()
    print("Read {} bytes".format(len(data)))

    if offset > len(data):
        print("Offset {} is not inside binary! Aborting..".format(offset))
        exit(-1)

    if offset + len(values) > len(data):
        print("Not enough room to insert bytes! Aborting..")
        exit(-1)

    print("Changing values at {} to {}".format(offset, offset + len(values)))
    for i in range(len(values)):
        data[offset + i] = values[i]

    print("Writing new data")
    f = open(binary, mode = "wb")
    f.write(data)
    f.close()
