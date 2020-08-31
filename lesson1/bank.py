'''
4) Реализовать функцию bank, которая приннимает следующие
аргументы: сумма депозита, кол-во лет, и процент. Результатом
выполнения должна быть сумма по истечению депозита
'''
from time import sleep

user_amount = int(input('Вас вітає ПривітБанк! Введіть суму депозиту: '))
user_years = int(input('На скільки років?: '))
user_rate = int(input('Введіть ставку у процентах (наприклад, 5, 19): '))


# note: ставка в процентах, т.е 5, 19, а не 0.05, 0.19
def bank(amount, years, rate):
    if 0 not in [amount, years, rate]:
        print(f'Отже, сума депозиту: {amount}\n')
        print(f'Кількість років {years}\n')
        print(f'Процентна ставка: {rate}\n')

        for i in range(years):
            amount += amount*(rate/100)

        print('Зачекайте, будь ласка... Обраховую суму...')
        print('...\n')
        sleep(1)
        print('...\n')
        sleep(1)
        print('...\n')
        sleep(1)
        print('...\n')
        print(f'Ваша фінальна сума становитиме {amount} гривень!')
    else:
        print('На жаль, ви не можете оформити депозит із такими умовами :(')

bank(user_amount, user_years, user_rate)
