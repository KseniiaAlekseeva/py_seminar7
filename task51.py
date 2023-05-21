orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# square = [el[0]*el[1] for el in orbits if el[0] != el[1]]

print(max(orbits, key=lambda x: x[0]*x[1] if x[0] != x[1] else 0))
