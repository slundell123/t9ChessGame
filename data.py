import bz2
import csv
import os

from functools import partial

def readlines():
    with open(os.path.abspath(filename), 'rb') as file:
        try:
            for row in csv.reader(_line_reader(file)):
                yield row
        except EOFError:
            return
def _line_reader(file):
    buffer = ''
    decompressor = bz2.BZ2Decompressor()
    reader = partial(file.read, buffer_size)
    for bindata in iter(reader, b''):
        block = decompressor.decompress(bindata).decode("utf-8")
        buffer += block
        if '\n' in buffer:
            lines = buffer.splitlines(True)
            if lines:
                buffer = '' if lines[-1].endswith('\n') else lines.pop()
                for line in lines:
                    yield line

filename = "lichess_db_puzzle.csv.bz2"
buffer_size = 4*1024

puzzlesWithinRange = []
for row in readlines():
    puzzlesWithinRange.append(row)

print(puzzlesWithinRange[0:10])

        