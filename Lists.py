
#exercises 3-4 -> 3-7
dinnerGuests = ['kirsten','boris','onkel leo']
print(f"\n{dinnerGuests[0].title()}, {dinnerGuests[1].title()} og {dinnerGuests[2].title()} er meget velkomne til mit middagsbord")
print(f"\nDesvaerre kan {dinnerGuests[2]} ikke vaere tilstede...")
dinnerGuests.remove('onkel leo')
dinnerGuests.append('Andreas')
print(f"Istedet har jeg blandt andre inviteret {dinnerGuests[2].title()}")
dinnerGuests.insert(0, "louis")
dinnerGuests.insert(2, "miriam")
print(f"Listen bestaar nu af {dinnerGuests}")
print("\nJeg kan desvaerre kun invitere 2 personer, da mit nye bord ikke ankom i tide")
dinnerGuests.pop()
dinnerGuests.pop()
dinnerGuests.pop()
print(dinnerGuests)
del dinnerGuests[0]
del dinnerGuests[0]
print(dinnerGuests)

# Organizing a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
cars.reverse()
print(cars)

# Exercise 3-8

locations = ['hawaii','portugal','china','gran canaria','new zealand']
print(locations)
print(sorted(locations))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)
