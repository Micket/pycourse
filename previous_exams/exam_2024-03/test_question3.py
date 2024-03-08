print(IPAddress((129,16,225,208)))

assert (IPAddress((129,16,225,204)) < IPAddress((129,16,230,1))) == True
assert (IPAddress((129,16,225,204)) == IPAddress((130,16,225,204)) == False

ip_range = IPRange(IPAddress((129,17,1,1)), IPAddress((129,17,3,32)))
print(f"{ip_range} has {len(ip_range)} addresses")

ip_range2 = IPRange(IPAddress((129,17,1,254)), IPAddress((129,17,2,3)))
for ip in ip_range2:
    print(ip)

print(len(ip_range2))

