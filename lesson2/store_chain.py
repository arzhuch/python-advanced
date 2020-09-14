'''
2) Создать класс магазина. Конструктор должен инициализировать
значения: «Название магазина» и «Количество проданных
товаров». Реализовать методы объекта, которые будут увеличивать
кол-во проданных товаров, и реализовать вывод значения
переменной класса, которая будет хранить общее количество
товаров проданных всеми магазинами.
'''


class Store:
    chain_sales = 0

    def __init__(self, store_name, sales_count=0):
        self.store_name = store_name
        self.sales_count = sales_count

        Store.chain_sales += sales_count

    def retail_sale(self, units_count):
        increment = units_count * 10
        self.sales_count += increment
        Store.chain_sales += increment
        print(f'{units_count} units 10 items each sold at {self.store_name}')

    def wholesale(self, pallets_count):
        increment = pallets_count * 100
        self.sales_count += increment
        Store.chain_sales += increment
        print(f'{pallets_count} pallets 100 items each sold at {self.store_name}')


if __name__ == '__main__':
    silpo = Store('Silpo', 0)
    silpo.retail_sale(10)
    print(f'Silpo local sales:  {silpo.sales_count}')
    auchan = Store('Auchan', 0)
    auchan.wholesale(5)
    print(f'Auchan local sales: {auchan.sales_count}')
    print(f'Global sales: {Store.chain_sales}')

