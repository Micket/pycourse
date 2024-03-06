class IPAddress:
    def __init__(self, vals: tuple):
        for val in vals:
            if val < 0 or val > 255:
                raise ValueError("IP segment out of range 0-255")
        self.vals = vals

    def __lt__(self, other):
        return self.vals < other.vals

    def __eq__(self, other):
        return self.vals == other.vals

    def __getitem__(self, i):
        return self.vals[i]

    def __str__(self):
        return '{}.{}.{}.{}'.format(*self.vals)

class IPMask:
    def __init__(self, vals: tuple, maskbits: int):
        self.vals = vals
        self.maskbits = maskbits

        mask_val = 0
        for i in range(maskbits):
            mask_val = mask_val * 2 + 1

        mask = []
        for group in range(4):
            mask.append(self.__mask_group(mask_val, group))
        mask.reverse()

        self.__mask = tuple(mask)
        self.__masked_vals = self.__mask_vals(self.vals)


    @staticmethod
    def __mask_group(val: int, group: int) -> int:
        factor = 256**group
        return int((val & 255 * factor) / factor)


    def __str__(self):
        return '{}.{}.{}.{}/{}'.format(*self.vals, self.maskbits)


    def mask_address(self, ipaddr: IPAddress) -> IPAddress:

        return IPAddress(self.__mask_vals(ipaddr.vals))

    def __mask_vals(self, vals: tuple) -> tuple:
        masked = []
        for m, v in zip(self.__mask, vals):
            masked.append(m | v)

        return masked        


    def in_mask(self, ipaddr: IPAddress) -> bool:
        for m, a in zip(self.__masked_vals, ipaddr.vals):
            if m | a != m:
                return False

        return True

class IPRange:
    def __init__(self, start: IPAddress, end: IPAddress):
        if end < start:
            raise ValueError("End address is smaller than start address!")

        self.start = start
        self.end = end

    def __str__(self):
        return '{} - {}'.format(self.start, self.end)

    def __len__(self):
        diff = [a-b for a, b in zip(self.end.vals, self.start.vals)]
        return sum([d*256**i for i, d in enumerate(reversed(diff))])

    def __iter__(self):
        class IPRangeIter:
            def __init__(self, iprange):
                self.current = iprange.start
                self.end = iprange.end

            def __next__(self):
                if self.current == self.end:
                    raise StopIteration

                # No need to be elegant
                a, b, c, d = self.current.vals
                d += 1
                if d == 256:
                    d = 0
                    c += 1
                if c == 256:
                    c = 0
                    b += 1
                if b == 256:
                    b = 0
                    a += 1

                ip = self.current
                self.current = IPAddress((a, b, c, d))
                return ip

        return IPRangeIter(self)

m1 = IPMask((129,16,1,1),32)
m2 = IPMask((129,16,1,1),16)
m3 = IPMask((129,16,1,1),15)
m4 = IPMask((129,16,1,1),12)

a1 = IPAddress((129,16,1,1))
a2 = IPAddress((129,17,254,10))
a3 = IPAddress((129,16,1,32))

print(a1, m2, m2.mask_address(a1))
print(a1, m4, m4.mask_address(a1))

print(a2, m2, m2.mask_address(a1))
print(a2, m4, m4.mask_address(a1))

r1 = IPRange(a1, a3)
print(r1, len(r1))

for i in r1:
    print(i)

print(a2, m2, m2.in_mask(a2))
print(a1, m1, m1.in_mask(a1))
