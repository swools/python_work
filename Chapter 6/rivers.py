rivers = {'nile': 'egypt', 'amazon':'brazil', 'mississippi': 'united states'}

for river in rivers:
    print(f"The {river.title()} runs through {rivers[river].title()}")

for key in rivers.keys():
    print(f"\n{key.title()}")

for value in rivers.values():
    print(f"\n{value.title()}")