import re
import collections


# Part A
def extract_links(s):
    links = []
    # You can piece together this with regexp or split if you want as well.
    # Here i demonstrate the "find" functionality which you might not have seen.
    pos = 0
    while True:
        pos = s.find('<a href="', pos)
        if pos == -1: # This means that there were no more substrings
            break
        # len('<a href="') == 9 so we skip ahead 8 positions to the link part:
        pos += 9
        endpos = s.find('"', pos)
        links.append(s[pos:endpos])
        pos = endpos # Start from here next search

    return links

x = extract_links('Links to <a href="http://www.amazon.co.uk/gp/deals">amazon deals</a> and <a href="www.google.com">google</a>')
print(x)


# Part A alternative
def extract_links2(s):
    return re.findall('<a href="(.*?)">', s, re.IGNORECASE)

x = extract_links2('Links to <a href="http://www.amazon.co.uk/gp/deals">amazon deals</a> and <a href="www.google.com">google</a>')
print(x)


# Part B
def extract_domain(link):
    # Split on :// and take the last part, and split that on / and take the first part:
    return link.split('://')[-1].split('/')[0]

a = extract_domain('https://www.amazon.co.uk')
b = extract_domain('http://www.foo.org/stuff/index.html')
c = extract_domain('google.se/search?q=kitten')
print(a)
print(b)
print(c)


# Part C
counter = collections.Counter()
with open('links.html') as f:
    for s in f:
        links = extract_links(s)
        domains = [extract_domain(link) for link in links]
        for d in domains:
            counter[d] += 1

# Printing:
domainwidth = max([len(x) for x in counter.keys()])
countwidth = max([len(str(x)) for x in counter.values()])

# Account for top row
domainwidth = max(domainwidth, 6)
countwidth = max(countwidth, 5)

# It is not necessary to sort these for the question, but it looks nicer that way.
# So you can do a reverse sort on the second index (the count)
sd = sorted(list(counter.items()), key=lambda x: x[1], reverse=True)

print('| ' + 'Domain' + ' '*(domainwidth-6) + ' | ' + 'Links' + ' '*(countwidth-5) + ' |')
print('+-' + '-'*domainwidth + '-+-' + '-'*countwidth + '-+')

for l, c in sd: # You could just loop over counter.items()
    print('| ' + l + ' '*(domainwidth-len(l)) + ' | ' + ' '*(countwidth-len(str(c))) + str(c) + ' |')
