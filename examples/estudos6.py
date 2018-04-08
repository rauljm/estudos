from collections import ChainMap

x = {'a': 1, 'b': 2}
y = {'a': 3, 'c': 4}

chainedmap = ChainMap(x, y)
print(chainedmap)

x['a'] = 10
print(chainedmap)

with_new_child = chainedmap.new_child()
with_new_child['x'] = 4

print(chainedmap)
print(with_new_child)

print(chainedmap.parents)
print(with_new_child.parents)
