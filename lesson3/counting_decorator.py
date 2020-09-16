'''Создать декоратор, который принимает на вход аргумент «количество
повторений». Который будет вызывать функцию, определенное кол-во
раз. Декорируемая функция должна возвращать:
1) Количество времени затраченное на каждый вызов;
2) Количество времени затраченное в общей сложности на все
вызовы;
3) Имя декорируемой функции;
4) Значение последнего результата выполнения.
'''

from time import time
from datetime import datetime, timedelta
from pprint import pprint

def repetition(number_of_calls):

    def proxy_decorator(func):

        def wrapper(*args, **kwargs):

            total_execution_time = 0
            calls_time_data = {}
            call_counter = 0

            if not number_of_calls > 0:
                raise ValueError("you can't call function zero times!")

            for i in range(number_of_calls):
                call_counter += 1

                print('function started...')
                start = time()
                result = func(*args, **kwargs)
                end = time()
                print('function ended')

                singe_execution_time = end - start
                calls_time_data[f'Call # {call_counter}'] = singe_execution_time
                total_execution_time += singe_execution_time

            return {
                'function result': result,
                'function name': func.__name__,
                'total execution_time': total_execution_time,
                'execution time per call': calls_time_data,
                'last execution time': singe_execution_time,
                }

        return wrapper

    return proxy_decorator


@repetition(2)
def my_func(a, b, c=0):
    return a + b + c

pprint(my_func(10, 20, 30))

@repetition(0)
def string_func(string1, string2):
    return string1 + string2

pprint(string_func('petro', 'poroshenko'))
