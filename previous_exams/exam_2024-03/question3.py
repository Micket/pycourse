class IPAddress:
    def __init__(self, vals: tuple):
        if len(vals) != 4:
            raise ValueError("The address must be made up of four parts")

        for val in vals:
            if val < 0 or val > 255:
                raise ValueError("IP segment out of range 0-255")
        self.vals = vals

    def __lt__(self, other):
        return self.vals < other.vals

    def __eq__(self, other):
        return self.vals == other.vals

    #def __getitem__(self, i):
    #    return self.vals[i]

    def __str__(self):
        return '{}.{}.{}.{}'.format(*self.vals)


class IPRange:
    def __init__(self, start: IPAddress, end: IPAddress):
        if not end > start:
            raise ValueError("End address is smaller or equal than start address!")

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


# Test code
print(IPAddress((129,16,225,208)))

assert (IPAddress((129,16,225,204)) < IPAddress((129,16,230,1))) == True
assert (IPAddress((129,16,225,204)) == IPAddress((130,16,225,204))) == False

ip_range = IPRange(IPAddress((129,17,1,1)), IPAddress((129,17,3,32)))
print(f"{ip_range} has {len(ip_range)} addresses")

ip_range2 = IPRange(IPAddress((129,17,1,254)), IPAddress((129,17,2,3)))
for ip in ip_range2:
    print(ip)

print(len(ip_range2))
