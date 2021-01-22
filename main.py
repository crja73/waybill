import random


cities = {'Алтуфьево - Можайка': 36, 'Алтуфьево - Румянцево': 46, 'Алтуфьево - Подольск': 74, 'Алтуфьево - МейлРУ': 25, 'Можайка - Румянцево': 15, 'Можайка - Подольск': 45, 'Можайка - МейлРУ': 21, 'Румянцево - Подольск': 43, 'Румянцево - МейлРУ': 27, 'Подольск - МейлРУ': 50}
cities2 = {'Алтуфьево - Можайка': 36, 'Алтуфьево - Румянцево': 46, 'Алтуфьево - Подольск': 74, 'Алтуфьево - МейлРУ': 25}
cities3 = {'Можайка - Румянцево': 15, 'Можайка - Подольск': 45, 'Можайка - МейлРУ': 21, 'Можайка - Алтуфьево': 36}
cities4 = {'Румянцево - Подольск': 43, 'Румянцево - МейлРУ': 27, 'Румянцево - Алтуфьево': 46, 'Румянцево - Можайка': 15}
cities5 = {'МейлРУ - Румянцево': 27, 'МейлРУ - Алтуфьево': 25, 'МейлРУ - Можайка': 21, 'МейлРУ - Подольск': 50}
cities6 = {'Подольск - Алтуфьево': 74, 'Подольск - МейлРУ': 50, 'Подольск - Румянцево': 43, 'Подольск - Можайка': 45}
num = 1500  # Нужное количество километров
count = 0  # подсчет километрожа
city, km = random.choice(list(cities2.items()))
copy1 = city
copy2 = km
print('{}   {}'.format(city, km))

count += km
spis = []

spis.append(city.split(' - ')[1])


while count < 1000:
	circle = random.randint(1, 3)
	print(circle)
	if circle == 1:
		string = spis[-1]
		a = copy1.split(' - ')[0]
		b = copy1.split(' - ')[1]
		print('{} - {}  {}'.format(b, a, km))
		count += km
		copy1 = b + ' - ' + a
		copy2 = km
		spis.append(a)

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

		print('{}   {}'.format(city, km))
		copy1 = city
		copy2 = km
		spis.append(city.split(' - ')[-1])
		for key, val in cities2.items():
			if spis[-1] in key:
				q = key.split(' - ')[0]
				w = key.split(' - ')[1]


		print('{} - {}   {}'.format(w, q, val))
		copy1 = w +' - ' + q
		copy2 = km
		spis.append(q)

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

		print('{}   {}'.format(city, km))
		copy1 = city
		copy2 = km
		spis.append(city.split(' - ')[-1])
		for key, val in cities.items():
			if spis[-1] in key:
				q = key.split(' - ')[0]
				w = key.split(' - ')[1]


		print('{} - {}   {}'.format(w, q, val))
		copy1 = w + ' - ' + q
		copy2 = km
		spis.append(q)
		for key, val in cities2.items():
			if spis[-1] in key:
				q = key.split(' - ')[0]
				w = key.split(' - ')[1]


		print('{} - {}   {}'.format(w, q, val))
		copy1 = w +' - ' + q
		copy2 = km
		spis.append(q)