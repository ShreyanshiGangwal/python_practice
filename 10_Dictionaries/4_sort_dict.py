# Sort dictionary by values...

d = {'a': 30, 'b': 10, 'c': 20}

sort_dict = dict(sorted(d.items(), key = lambda x: x[1]))

print(sort_dict)