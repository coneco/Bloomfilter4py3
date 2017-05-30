'''The Bloomfilter class file.'''

from bitlist import BitList

class Bloomfilter:
    '''The Bloomfilter class.'''

    def __init__(self, nbits, nhashs):
        self.nbits = nbits
        self.nhashs = nhashs
        self.bucket = BitList(nbits)

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
