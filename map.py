obj1 = { 'a': 1, 'b': 2, 'c': 3}
obj2 = { 'a': 4, 'b': 5, 'c': 6}
obj3 = { 'a': 7, 'b': 8, 'c': 9}
obj4 = { 'a': 10, 'b': 11, 'c': 12}

l = [obj1, obj2, obj3, obj4]

print(l)


def getProps(item):
    d = {}
    d['a'] = item['a']
    d['b'] = item['b']

    return d

l_mapped = map(getProps, l)

print(l_mapped)

