s = Schedule(10)
print(s.is_available(6))
s.reserve(3, "Thomas")
s.reserve(6, "Micke")
print(s.is_available(6))

for slot_id, name in s.reserved():
    print("{} is reserved by {}".format(slot_id, name))
    if s.is_available(8):
        s.reserve(8, "Thomas")
