class TNumber:
    def __init__(self, num):
        self.num = num

    def sum_digit(self):
        pass

    @property
    def first_digit(self):
        pass

    @property
    def last_digit(self):
        pass

class TIntNumber(TNumber):

    def sum_digit(self):
        return sum(map(int, list(str(super().num))))

    @property
    def first_digit(self):
        return int(list(str(super().num))[0])

    @property
    def last_digit(self):
        return int(list(str(super().num))[-1])

class TRealNumber(TNumber):

    def sum_digit(self):
        return sum(map(float, [i for i in str(super().num) if i != '.']))

    @property
    def first_digit(self):
        return int(list(str(super().num))[0])

    @property
    def last_digit(self):
        return int(list(str(super().num))[-1])