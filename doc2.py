a=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
b=''.join(''.join(l)for l in a)
print(b)