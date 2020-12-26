class TSquare:

    def __init__(self, side_len = 0):
        if side_len < 0:
            raise Exception('Side length should be positive')
        else:
            self.__side_len = side_len

    @property
    def side_length(self):
        return self.__side_len

    @side_length.setter
    def side_length(self, x):
        if x < 0:
            raise Exception('Side length should be positive')
        else:
            self.__side_len = x

    @property
    def square_area(self):
        return self.__side_len ** 2

    @property
    def square_perimeter(self):
        return self.__side_len * 4

    def enter_side(self):
        self.side_length = float(input("Enter side length: "))

    def show_side(self):
        print(self.side_length)

    def __lt__(self, other):
        return self.square_area < other.square_area

    def __le__(self, other):
        return self.square_area <= other.square_area

    def __eq__(self, other):
        return self.square_area == other.square_area

    def __ne__(self, other):
        return self.square_area != other.square_area

    def __gt__(self, other):
        return self.square_area > other.square_area

    def __ge__(self, other):
        return self.square_area >= other.square_area

    def __add__(self, other):
        return TSquare(self.side_length + other.side_length)

    def __sub__(self, other):
        return TSquare(self.side_length - other.side_length)

    def __mul__(self, other):
        return TSquare(self.side_length * other)

class TCube(TSquare):

    @property
    def cube_area(self):
        return 6 * (super().side_length ** 2)

    @property
    def cube_perimeter(self):
        return super().side_length * 12

if __name__ == "__main__":
    #-------Square-------

    s = TSquare(5.3)

    print('Square #1 side length = ', s.side_length)
    print('Square #1 area = ', s.square_area)
    print('Square #1 perimeter = ', s.square_perimeter)

    s1 = TSquare(7.1)

    print('Square #2 side length = ', s1.side_length)
    print('Square #2 side length = ', s1.square_area)
    print('Square #2 side length = ', s1.square_perimeter)

    print(s < s1)
    print(s <= s1)
    print(s >= s1)
    print(s > s1)
    print(s != s1)
    print(s == s1)

    s.enter_side()
    s.show_side()

    #-------Cube-------

    c = TCube(5.3)

    print('Cube #1 side length = ', c.side_length)
    print('Cube #1 area = ', c.cube_area)
    print('Cube #1 perimeter = ', c.cube_perimeter)

    c1 = TCube(7.1)

    print('Cube #2 side length = ', c1.side_length)
    print('Cube #2 area = ', c1.cube_area)
    print('Cube #2 perimeter = ', c1.cube_perimeter)

    print(c < c1)
    print(c <= c1)
    print(c >= c1)
    print(c > c1)
    print(c != c1)
    print(c == c1)

    c.enter_side()
    c.show_side()