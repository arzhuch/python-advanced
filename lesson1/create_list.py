'''
1)Создать список из N элементов (от 0 до n с шагом 1).
В этом списке вывести все четные значения.
'''


limit = 51

my_list = list(range(limit))

for i in my_list:
    if i % 2 == 0:
        print(i)
