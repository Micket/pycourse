class IPAddress:
    def __init__(self, vals):
        self.vals = vals

    def __eq__(self, other):
        return self.vals == other.vals

    def __str__(self):
        return '{}.{}.{}.{}'.format(*self.vals)

class IPMask:
    def __init__(self, vals, maskbits):
        self.vals = vals
        self.maskbits = maskbits

    def __str__(self):
        return '{}.{}.{}.{}/{}'.format(*self.vals, mask)

    def __in__(self, ipaddr):
        val_mask = [v*256 for v in enumerate(self.vals)]
        val_ip = [v*256 for v in enumerate(ipaddr.vals)]
        


    def __iter__(self):
        pass # This could be quite tricky to implement.

class IPRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        if s, e in zip(self.start, self.end):
            if e < s:
                raise ValueError("End range is smaller than start"

    def __str__(self):
        return '{}.{}.{}.{}-{}.{}.{}.{}'.format(*self.start, *self.end)

    def __len__(self):
        diff = [a-b for a, b in zip(self.end, self.start)]
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
                a, b, c, d = self.current
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

                ip = IPAddress(self.current)
                self.current = (a, b, c, d)
                return ip

        return IPRangeIter(self)
