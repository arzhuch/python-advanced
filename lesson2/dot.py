class Dot:

    def __init__(self, x, y, z):

        self._x = x
        self._y = y
        self._z = z

    class Decorators:

        @classmethod
        def type_checker(cls, _type):

            def proxy_decorator(decorated):

                def wrapper(self, checked_value):
                    print('decoration')
                    if not isinstance(checked_value, _type):
                        raise ValueError(f'Unsupported type passed while interaction with Dots: requiered {_type}')
                    result = decorated(self, checked_value)
                    print('successful decoration')
                    return result

                return wrapper

            return proxy_decorator

    def get_x(self):
        return self._x

    @Decorators.type_checker((int, float))
    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    @Decorators.type_checker((int, float))
    def set_y(self, value):
        self._y = value

    def get_z(self):
        return self._z

    @Decorators.type_checker((int, float))
    def set_z(self, value):
        self._z = value

    # @Decorators.type_checker('Dot') - //TODO how to handle this ?
    def __add__(self, other):

        new_x = self._x + other._x
        new_y = self._y + other._y
        new_z = self._z + other._z

        print('Returning sum of two Dots:\n', new_x, new_y, new_z)

        return Dot(new_x, new_y, new_z)

    # @Decorators.type_checker(Dot)
    def __mul__(self, other):

        new_x = self._x * other._x
        new_y = self._y * other._y
        new_z = self._z * other._z

        print('Returning product of two Dots:\n', new_x, new_y, new_z)

        return Dot(new_x, new_y, new_z)

    # @Decorators.type_checker(Dot)
    def __sub__(self, other):

        new_x = self._x - other._x
        new_y = self._y - other._y
        new_z = self._z - other._z

        print('Returning substraction result of two Dots:\n', new_x, new_y, new_z)

        return Dot(new_x, new_y, new_z)

    # @Decorators.type_checker(Dot)
    def __truediv__(self, other):

        new_x = self._x / other._x
        new_y = self._y / other._y
        new_z = self._z / other._z

        print('Returning quotient of two Dots:\n', new_x, new_y, new_z)

        return Dot(new_x, new_y, new_z)

    # @Decorators.type_checker(Dot)
    def __neg__(self):

        new_x = - self._x
        new_y = - self._y
        new_z = - self._z

        print('Returning negative Dot:\n', new_x, new_y, new_z)

        return Dot(new_x, new_y, new_z)


a = Dot(1, 3, 5)
a.set_x(3)
b = 10
c = a + b
print(type(a))
