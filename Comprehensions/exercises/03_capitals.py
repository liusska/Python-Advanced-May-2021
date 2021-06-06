countries = input().split(', ')
cities = input().split(', ')

print(''.join([f'{country} -> {city}\n' for country, city in zip(countries, cities)]))
