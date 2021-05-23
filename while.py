import os
os.system('cls')


edad = input('Su edad?: ')
edad = int(edad)

''''
if edad < 18:
	print('Es un bebe')
else:
	print('Es un mayor')
'''

if edad <= 2:
	print('Es un bebe')
elif edad <= 12:
	print('Es un niño')
elif edad <= 18:
	print('Es un adolecente')
elif edad <= 39:
	print('Es un adulto')
elif edad <= 64:
	print('Es un adulto maduro')
elif edad <= 65:
	print('Es un adulto mayor')
else:
	print('Es un menor de edad')