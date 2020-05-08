#/usr/bin/env python3

x = 0
y = 1
count = 1

print("0: 0")
print("1: 1")
for count in range(2, 100):
	y += x
	x = y - x
	print(str(count) + ": " + str(y))
