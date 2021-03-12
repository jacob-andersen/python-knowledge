a = True
b = False

print (not a or b == a^b)
print ((a or b) and not (a and b) == a^b)
print ((a and b) or not (a or b) == a^b)
print ((a and not b) or (not a and b)== a^b)
print (a and not b == a^b)

