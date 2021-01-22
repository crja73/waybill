import random


cities = {'Алтуфьево - Можайка': 36, 'Алтуфьево - Румянцево': 46, 'Алтуфьево - Подольск': 74, 'Алтуфьево - МейлРУ': 25, 'Можайка - Румянцево': 15, 'Можайка - Подольск': 45, 'Можайка - МейлРУ': 21, 'Румянцево - Подольск': 43, 'Румянцево - МейлРУ': 27, 'Подольск - МейлРУ': 50}
cities2 = {'Алтуфьево - Можайка': 36, 'Алтуфьево - Румянцево': 46, 'Алтуфьево - Подольск': 74, 'Алтуфьево - МейлРУ': 25}
num = 1500  # Нужное количество километров
count = 0  # подсчет километрожа
city, km = random.choice(list(cities2.items()))
copy1 = city
copy2 = km
print('{}   {}'.format(city, km))

count += km
spis = []

spis.append(city.split(' - ')[1])

while count < 80:
	circle = random.randint(1, 1)
	if circle == 1:
		a = copy1.split(' - ')[0]
		b = copy1.split(' - ')[1]
		print('{} - {}  {}'.format(b, a, km))
		count += km
		copy1 = b + ' - ' + a

	elif circle == 2:
		while city == copy1 and km == copy2 and copy1.split(' - ')[1] != city.split(' - ')[0]:
			city, km = random.choice(list(cities.items()))
			
