import os
os.system('cls')

print("Other thinks")

edad = input('Su edad?: ')
edad = int(edad)

if edad < 18:
	print('Es un bebe')
else:
	print('Es un mayor')