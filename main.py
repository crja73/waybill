import random
import pandas as pd


def func():

	al = {'Алтуфьево - Можайка': 36, 'Алтуфьево - Румянцево': 46, 'Алтуфьево - Подольск': 74, 'Алтуфьево - МейлРУ': 25, 'Можайка - Румянцево': 15, 'Можайка - Подольск': 45, 'Можайка - МейлРУ': 21, 'Румянцево - Подольск': 43, 'Румянцево - МейлРУ': 27, 'Румянцево - Можайка': 15, 'МейлРУ - Румянцево': 27, 'МейлРУ - Можайка': 21, 'МейлРУ - Подольск': 50, 'Подольск - МейлРУ': 50, 'Подольск - Румянцево': 43, 'Подольск - Можайка': 45}

	cities2 = {'Алтуфьево - Можайка': 36, 'Алтуфьево - Румянцево': 46, 'Алтуфьево - Подольск': 74, 'Алтуфьево - МейлРУ': 25}
	cities3 = {'Можайка - Румянцево': 15, 'Можайка - Подольск': 45, 'Можайка - МейлРУ': 21}
	cities4 = {'Румянцево - Подольск': 43, 'Румянцево - МейлРУ': 27, 'Румянцево - Можайка': 15}
	cities5 = {'МейлРУ - Румянцево': 27, 'МейлРУ - Можайка': 21, 'МейлРУ - Подольск': 50}
	cities6 = {'Подольск - МейлРУ': 50, 'Подольск - Румянцево': 43, 'Подольск - Можайка': 45}
	print('Введите километраж')
	num = 1500  # Нужное количество километров
	count = 0  # подсчет километрожа
	city, km = random.choice(list(cities2.items()))
	copy1 = city
	copy2 = km

	#/////////////////////////
	print('{}   {}'.format(city, km))
	#////////////////////////

	global sponge
	global sporge
	global stronge

	sponge = []
	sporge = []
	stronge = []
	sponge.append(city.split(' - ')[0])
	stronge.append(city.split(' - ')[1])
	sporge.append(km)

	count += km
	spis = []

	spis.append(city.split(' - ')[1])


	while count < (num - 50):

		circle = random.randint(1, 3)

		if circle == 1:
			string = spis[-1]
			a = copy1.split(' - ')[0]
			b = copy1.split(' - ')[1]
			#////////////////////////
			print('{} - {}  {}'.format(b, a, km))
			#////////////////////////
			count += km
			copy1 = b + ' - ' + a
			copy2 = km
			spis.append(a)
			sponge.append(b)
			stronge.append(a)
			sporge.append(km)
			if count >= (num - 50):
				print('Лооол')
				break

		elif circle == 2:
			if spis[-1] == 'Можайка':
				city, km = random.choice(list(cities3.items()))
				copy1 = city
				copy2 = km

			elif spis[-1] == 'Подольск':
				city, km = random.choice(list(cities6.items()))
				copy1 = city
				copy2 = km

			elif spis[-1] == 'МейлРУ':
				city, km = random.choice(list(cities5.items()))
				copy1 = city
				copy2 = km

			elif spis[-1] == 'Румянцево':
				city, km = random.choice(list(cities4.items()))
				copy1 = city
				copy2 = km

			elif spis[-1] == 'Алтуфьево':
				city, km = random.choice(list(cities2.items()))
				copy1 = city
				copy2 = km

			else:
				print('Error!, Try again!')

			#////////////////////////
			print('{}    {}'.format(city, km))
			#////////////////////////
			copy1 = city
			copy2 = km
			count += km
			spis.append(city.split(' - ')[-1])

			sponge.append(city.split(' - ')[0])
			stronge.append(city.split(' - ')[1])

			sporge.append(km)
			if count >= (num - 50):
				print('Лооол')
				break

			for key, val in cities2.items():
				if spis[-1] in key:
					q = key.split(' - ')[0]
					w = key.split(' - ')[1]
					po = val

			#////////////////////////
			print('{} - {}   {}'.format(w, q, po))
			#////////////////////////
			copy1 = w +' - ' + q
			copy2 = km
			count += po
			spis.append(q)
			sponge.append(w)
			stronge.append(q)
			sporge.append(po)
			if count >= (num - 50):

				break

		elif circle == 3:
			if spis[-1] == 'Можайка':
				city, km = random.choice(list(cities3.items()))
				copy1 = city
				copy2 = km

			elif spis[-1] == 'Подольск':
				city, km = random.choice(list(cities6.items()))
				copy1 = city
				copy2 = km

			elif spis[-1] == 'МейлРУ':
				city, km = random.choice(list(cities5.items()))
				copy1 = city
				copy2 = km

			elif spis[-1] == 'Румянцево':
				city, km = random.choice(list(cities4.items()))
				copy1 = city
				copy2 = km

			elif spis[-1] == 'Алтуфьево':
				city, km = random.choice(list(cities2.items()))
				copy1 = city
				copy2 = km

			else:
				print('Error!, Try again!')

			#////////////////////////
			print('{}   {}'.format(city, km))
			#////////////////////////
			copy1 = city
			copy2 = km
			count += km
			spis.append(city.split(' - ')[-1])

			sponge.append(city.split(' - ')[0])
			stronge.append(city.split(' - ')[1])

			sporge.append(km)
			if count >= (num - 50):
				print('Лооол')
				break

			for key, val in al.items():
				
				if spis[-1] == key.split(' - ')[0]:

					q = key.split(' - ')[0]
					w = key.split(' - ')[1]
					ji = val

			#////////////////////////
			print('{} - {}   {}'.format(q, w, ji))
			#////////////////////////
			copy1 = w + ' - ' + w
			copy2 = km
			count += ji
			spis.append(w)

			sponge.append(q)
			stronge.append(w)

			sporge.append(ji)
			if count >= (num - 50):
				print('Лооол')
				break
			for key, val in cities2.items():
				if spis[-1] in key:    # здесь нужно не сразу использовать места, а сначал собрать вместе, а потом выбрать из них на рандом, чтоб избежать многократных повторений
					q = key.split(' - ')[0]
					w = key.split(' - ')[1]
					pl = val

			#////////////////////////
			print('{} - {}   {}'.format(w, q, pl))
			#////////////////////////
			copy1 = w +' - ' + q
			copy2 = km
			count += pl
			spis.append(q)
			sponge.append(w)
			stronge.append(q)
			sporge.append(pl)
			if count >= (num - 50):
				print('Лооол')
				break

	if spis[-1] != 'Алтуфьево':
		for key, val in al.items():
			if 'Алтуфьево' in key and spis[-1] in key:
				km = val
		#////////////////////////
		print('{} - Алтуфьево   {}'.format(spis[-1], km))
		#////////////////////////
		count += km
		sponge.append(spis[-1])
		stronge.append('Алтуфьево')
		sporge.append(km)
	print(count)
	print(' ')
	print(sum(sporge))
	print(' ')
	print(sponge)
	print(sporge)

	if sum(sporge) > num:
		while sum(sporge) != num:
			km = random.randint(0, len(sporge) - 1)
			sporge[km] -= 1
	elif sum(sporge) < num:
		while sum(sporge) != num:
			km = random.randint(0, len(sporge) - 1)
			sporge[km] += 1
	else:
		pass
	print(sporge)
	print(sum(sporge))

	if count >= num + 15 or count <= num - 15:
		return False
	else:
		return True

def g():
	while func() != True:
		continue

g()
text = input('Если результат вас устравивает, то напишите латинскую букву "Y" и все данные внесутся в таблицу, если же результат вам не нравится, сгенерируете другую комбинацию, нажав латинскую "N" ->')
if text == 'Y':
	df = pd.DataFrame({'City_1': sponge, 'City_2': stronge, 'km': sporge})
	df.to_excel('./teams.xlsx')
elif text == 'N':
	pass
else:
	print("Выберите: Y/N")