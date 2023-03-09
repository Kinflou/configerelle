# Standard Imports
from typing import Iterator

# Local Imports

# External Imports
from flatdict import FlatDict


class DIter(Iterator):

    def __init__(self, dct: dict):
        self.dct = dct
        self.idx = 0

    def __next__(self):
        if len(self.dct) <= self.idx:
            raise StopIteration

        self.idx += 1
        yield


if __name__ == '__main__':
    test = {
        'some': {
            'thing': {},
            'any': {}
        },
        'other': {},
        'another': {
            'texts': ['foo', 'bar'],
        }
    }

    flat = FlatDict(test)
    ...

