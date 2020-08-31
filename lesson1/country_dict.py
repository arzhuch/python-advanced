'''
2) Создать словарь Страна:Столица. Создать список стран. Не все
страны со списка должны сходиться с названиями стран со словаря. С
помощою оператора in проверить на вхождение элемента страны в
словарь, и если такой ключ действительно существует вывести
столицу.
'''
from pprint import pprint

country_dict = {
    "Ukraine": "Kyiv",
    "Poland": "Warsaw",
    "Slovakia": "Bratislava",
    "Turkey": "Istanbul",
    "USA": "Washington",
    "UK": "London",
    "Germany": "Berlin"
}

print(f"\nDict: \n")
pprint(country_dict)


country_list = ["Poland", "Turkey", "Spain", "Portugal", "USA", "Germany", "Brazil"]

print(f"\nList: \n {country_list}\n")

for country in country_list:
    if country in country_dict:
        print(f"{country_dict.get(country)} is the capital of {country}")
    else:
        print(f"{country}: no such country in the list!")
