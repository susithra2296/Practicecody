
# n = 5

#increasing triangle
# for i in range(n):
# 	for j in range(i+1):
# 		print("*", end= " ")
# 	print()

#decreasing triangle
# for i in range(n):
# 	for j in range(i,n):
# 		print("*", end= " ")
# 	print()

# right side triangle
# for i in range(n):
# 	for j in range(i,n):
# 		print(" ", end= " ")
# 	for j in range(i+1):
# 		print("*", end= " ")
# 	print()

# left side triangle
# for i in range(n):
# 	for j in range(i+1):
# 		print(" ", end= " ")
# 	for j in range(i,n):
# 		print("*", end= " ")
# 	print()

# for i in range(n):
# 	for j in range(i,n):
# 		print(" ", end= " ")
# 	for j in range(i):
# 		print("*", end= " ")
# 	for j in range(i+1):
# 		print("*", end= " ")
# 	print()
#

# for i in range(n):
# 	for j in range(i,n):
# 		print(" ", end= " ")
# 	for j in range(i):
# 		print("*", end= " ")
# 	for j in range(i+1):
# 		print("*", end= " ")
# 	print()

n=5

for i in range(n-1):
	for j in range(i,n):
		print(" ", end= " ")
	for j in range(i):
		print("*", end= " ")
	for j in range(i+1):
		print("*", end= " ")
	print()
for i in range(n):
	for j in range(i+1):
		print(" ", end= " ")
	for j in range(i,n-1):
		print("*", end= " ")
	for j in range(i,n):
		print("*", end= " ")
	print()
