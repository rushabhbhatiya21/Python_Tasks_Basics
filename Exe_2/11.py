l1 = [1, 2, 3]
d1 = {1: 10, 2: 20, 3: 30}
s1 = {1, 2, 3}

l2, d2, s2 = l1, d1, s1

print(f'l1: {id(l1)}\nl2: {id(l2)}\n\nd1: {id(d1)}\nd2: {id(d2)}\n\ns1: {id(s1)}\ns2: {id(s2)}\n')
print(f'List: {id(l1) == id(l2)}')

