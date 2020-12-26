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


