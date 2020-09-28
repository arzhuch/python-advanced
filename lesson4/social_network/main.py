from time import sleep
from user import User
from operations import *


if __name__ == '__main__':
    while True:
        session = startup_selector()
        operations_selector(session)

