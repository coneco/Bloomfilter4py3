'''The Bloomfilter class file.'''

import struct
from bitlist import BitList

class Bloomfilter:
    '''The Bloomfilter class.'''

    __slots__ = ("nbits", "nhashs", "bucket")

    def __init__(self, nbits_or_filepath, nhashs = 1):
        if isinstance(nbits_or_filepath, int):
            self.nbits = nbits_or_filepath
            self.nhashs = nhashs
            self.bucket = BitList(nbits_or_filepath)
        elif isinstance(nbits_or_filepath, str):
            file = open(nbits_or_filepath, 'rb')
            self.nbits = struct.unpack('i', file.read(4))[0]
            self.nhashs = struct.unpack('i', file.read(4))[0]
            self.bucket = BitList(file.read())
            file.close()


    def add(self, item):
        if isinstance(item, str):
            item = item.encode("utf-8")
        locs = self._location(item)
        for loc in locs:
            self.bucket.set_bit(loc, 1)

    def test(self, item):
        if isinstance(item, str):
            item = item.encode("utf-8")
        locs = self._location(item)
        for loc in locs:
            if self.bucket.get_bit(loc) == 0:
                return False
        return True

    def save(self, filepath):
        file = open(filepath, 'wb')
        file.write(struct.pack('i', self.nbits) + struct.pack('i', self.nhashs) + self.bucket.main_object)
        file.close()

    def _location(self, item):
        def fnv_multiply(a):
            #return a * 16777619 % 2 ** 32
            return (a + (a << 1) + (a << 4) + (a << 7) + (a << 8) + (a << 24)) & 0xffffffff

        def fnv_mix(a):
            a += a << 13
            a ^= a >> 7
            a += a << 3
            a ^= a >> 17
            a += a << 5
            return a & 0xffffffff

        def fnv_1a(item):
            ret_hash_a = 2166136261
            for i in item:
                ret_hash_a = fnv_multiply(ret_hash_a ^ i)
            return fnv_mix(ret_hash_a)

        def fnv_1a_b(ret_hash_a):
            return fnv_mix(fnv_multiply(ret_hash_a))

        ret_locations = []
        a_hash = fnv_1a(item)
        b_hash = fnv_1a_b(a_hash)
        a_hash %= self.nbits
        while len(ret_locations) < self.nhashs:
            ret_locations.append(a_hash)
            a_hash = (a_hash + b_hash) % self.nbits
        return ret_locations

    def __len__(self):
        return self.bucket.length

    def __repr__(self):
        return "<Bloomfilter with {:d} bits and {:d} hash functions>".format(self.nbits, self.nhashs)

    def __contains__(self, item):
        return self.test(item)
