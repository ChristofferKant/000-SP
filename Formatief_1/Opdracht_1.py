"""Versie 1 met 2 for loops"""
n = int(input("Hoe groot? "))
m = n
for n in range(1, n + 1):
	print("*" * n)

for m in range(m - 1, 0, -1):
	print("*" * m)

"""Omgekeerde versie met 2 for loops"""
n = int(input("Hoe groot? "))
m = n
for n in range(1, n + 1):
	print("{:>10}".format("*"*n))

for m in range(m - 1, 0, -1):
	print("{:>10}".format("*"*m))

"""Versie 1 met 2 while loops"""
n = int(input("Hoe groot? "))
m = 0
while m != n:
	print("*"*m)
	m += 1

while n != 0:
	print("*"*n)
	n -= 1

"""Omgekeerde versie met 2 while loops"""
n = int(input("Hoe groot? "))
m = 0
i = 2
x = n

while m != n:
	m += 1
	print(" " * x, "*" * m)
	x -= 1

while n != 0:
	n -= 1
	print(" " * i, "*" * n)
	i += 1

