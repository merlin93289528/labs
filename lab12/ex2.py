class TRational:
    def __init__(self, ch, zn):
        self.ch = ch
        self.zn = zn

    def add(self, num):
        self.ch += num.ch
        self.zn += num.zn

    def diff(self, num):
        self.ch -= num.ch
        self.zn -= num.zn

    def comp(self, num):
        self.ch *= num.ch
        self.zn *= num.zn

    def fract(self, num):
        self.ch /= num.ch
        self.zn /= num.zn

    def to_string(self):
        print(str(self.ch) + "/" + str(self.zn))

