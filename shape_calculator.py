class Rectangle(object):
    def __init__(self, width, height):
        self._width = width
        self._height = height
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def get_area(self):
        return self._width * self._height

    def get_perimeter(self):
        return 2 * self._width + 2 * self._height

    def get_diagonal(self):
        return (self._width ** 2 + self._height ** 2) ** .5

    def get_picture(self):
        if self._width > 50 or self._height > 50:
            return "Too big for picture."
        for i in range(self._height):
            for j in range(self._width):
                print('*',end='')
            print("\n")
        return ''

    def get_amount_inside(self, another_shape):
        if self._width >= another_shape.width and self._height >= another_shape.height:
            return int(self.get_area()/another_shape.get_area())
        return "Cannot fit."

    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self._width, self._height)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)
        self._side = side

    def set_side(self, side):
        self._side = side
        self.set_width(side)
        self.set_height(side)

    def __str__(self):
        return 'Square(side={})'.format(self._side)

def main():
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))

if __name__=='__main__':
    main()


