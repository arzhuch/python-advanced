class Dot:

    def __init__(self, x, y, z):

        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x

    def set_x(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Incorrect type assigned for coordinate x!')

    def get_y(self):
        return self._y

    def set_y(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Incorrect type assigned for coordinate y!')

    def get_z(self):
        return self._z

    def set_z(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Incorrect type assigned for coordinate z!')


    def __add__(self, other):
        if not isinstance(other, Dot):
            raise TypeError('You can add only Dots to Dots!')

        new_x = self._x + other._x
        new_y = self._y + other._y
        new_z = self._z + other._z

        print('Returning sum of two Dots:\n', new_x, new_y, new_z)

        return Dot(new_x, new_y, new_z)


    def __mul__(self, other):
        if not isinstance(other, Dot):
            raise TypeError('You can multiply only Dots by Dots!')

        new_x = self._x * other._x
        new_y = self._y * other._y
        new_z = self._z * other._z

        print('Returning product of two Dots:\n', new_x, new_y, new_z)

        return Dot(new_x, new_y, new_z)

    def __sub__(self, other):
        if not isinstance(other, Dot):
            raise TypeError('You can substract only Dots from Dots!')

        new_x = self._x - other._x
        new_y = self._y - other._y
        new_z = self._z - other._z

        print('Returning substraction result of two Dots:\n', new_x, new_y, new_z)

        return Dot(new_x, new_y, new_z)


    def __truediv__(self, other):
        if not isinstance(other, Dot):
            raise TypeError('You can divide only Dots by Dots!')

        new_x = self._x / other._x
        new_y = self._y / other._y
        new_z = self._z / other._z

        print('Returning quotient of two Dots:\n', new_x, new_y, new_z)

        return Dot(new_x, new_y, new_z)


    def __neg__(self):

        new_x = - self._x
        new_y = - self._y
        new_z = - self._z

        print('Returning negative Dot:\n', new_x, new_y, new_z)

        return Dot(new_x, new_y, new_z)
