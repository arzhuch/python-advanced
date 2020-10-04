"""
1) Создать декоратор, который будет запускать функцию в отдельном
потоке. Декоратор должен принимать следующие аргументы:
название потока, является ли поток демоном.
"""

from threading import Thread
from time import sleep


def separate_thread(func):
    def wrapper(*args, **kwargs):
        new_thread = Thread(target=func, args=args, kwargs=kwargs)
        new_thread.start()
        return new_thread
    return wrapper


def separate_thread_with_args(thread_name=None, is_daemon=False):
    def proxy(func):
        def wrapper(*args, **kwargs):
            new_thread = Thread(target=func, args=args, kwargs=kwargs, daemon=is_daemon)
            new_thread.name = thread_name
            new_thread.start()
            print(f"Thread {new_thread.name} has been created")
            return new_thread
        return wrapper
    return proxy
