class NotFreeException(Exception):
    pass

class NotAllocatedException(Exception):
    pass

class InvalidSlotException(Exception):
    pass

class Schedule:
    def __init__(self, no_slots):
        self._slots = [None] * no_slots

    def _check_id(self, slot_id):
        if slot_id < 0 or slot_id >= len(self._slots):
            raise InvalidSlotException("Invalid slot_id given:" + str(slot_id))

    def is_available(self, slot_id):
        self._check_id(slot_id)
        return self._slots[slot_id] is None

    def reserve(self, slot_id, name):
        if not self.is_available(slot_id):
            raise NotFreeException('Slot is already reserved by "' + self._slots[slot_id] + '"!')

        self._slots[slot_id] = name

    def release(self, slot_id):
        if self.is_available(slot_id):
            raise NotAllocatedException('Slot is not reserved!')

        self._slots[slot_id] = None

    def reserved(self):
        class ScheduleIterator():
            def __init__(self, slots):
                self.it = enumerate(slots)

            def __iter__(self):
                return self

            def __next__(self):
                while True:
                    slot_id, name = next(self.it)
                    if name is not None:
                        return slot_id, name

        return ScheduleIterator(self._slots)


s = Schedule(10)
print(s.is_available(6))
s.reserve(3, "Thomas")
s.reserve(6, "Micke")
print(s.is_available(6))

for slot_id, name in s.reserved():
    print("{} is reserved by {}".format(slot_id, name))
    if s.is_available(8):
        s.reserve(8, "Thomas")

try:
    s.reserve(3, "Krille")
except NotFreeException:
    pass

try:
    s.reserve(-1, "Krille")
except InvalidSlotException:
    pass
