# code to implement diff set methods 

s1 = {1, 6, 8, 9, 3}
s2 = {3, 5, 7, 8, 4}

print(s1.union(s2))
print(s1.intersection(s2))

print({1, 10}.issubset(s1))
print(s2.issuperset({3, 7, 4}))