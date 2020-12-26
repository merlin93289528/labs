class Rect:
    def __init__(self):
        self.__a = 0
        self.__b = 0

    def __getitem__(self, key):  # --- Для зчитування значення за індексом
        if key == 'a':
            return self.__a
        elif key == 'b':
            return self.__b
        else:
            raise Exception("Wrong key")

    def __setitem__(self, key, value):  # --- Для встановлення значення за індексом
        if value > 0:
            if key == 'a':
                self.__a = value
            elif key == 'b':
                self.__b = value
            else:
                raise Exception("Wrong key")
        else:
            raise Exception("Length must be bigger than zero")

    @property
    def perimetr(self):
        return (self.__a * 2) + (self.__b * 2)

    @property
    def square(self):
        return self.__a * self.__b
