class MyComplex:

    def __init__(self, rl, img):
        self.rl = rl
        self.img = img

    def __add__(self, other):
        new_rl = self.rl + other.rl
        new_img = self.img + other.img
        return MyComplex(new_rl, new_img)

    def __sub__(self, other):
        new_rl = self.rl - other.rl
        new_img = self.img - other.img
        return MyComplex(new_rl, new_img)

    def __mul__(self, other):
        res_rl = self.rl * other.rl - self.img * other.img
        res_img = self.rl * other.img + self.img * other.rl
        return MyComplex(res_rl, res_img)

    def __radd__(self, other):
        new_rl = self.rl + other
        return MyComplex(new_rl, new_rl)

    def __rsub__(self, other):
        new_rl = self.rl - other
        return MyComplex(new_rl, -self.img)

    def __rmul__(self, other):
        res_rl = other * self.rl
        res_img = other * self.img
        return MyComplex(res_rl, res_img)

    def __rdiv__(self, other):
        new_rl = self.rl / other
        return MyComplex(new_rl, self.img)

    def __str__(self):
        if self.img and self.rl and self.img > 0:
            return f'{self.rl}+{self.img}i'
        elif self.img and self.rl and self.img < 0:
            return f'{self.rl}{self.img}i'
        elif self.rl:
            return f'{self.rl}'
        elif self.img:
            return f'{self.img}i'
