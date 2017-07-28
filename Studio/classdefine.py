class Fraction(object):

    def __init__(self, top, bottom):
        self.num = top        #the numerator is on top
        self.den = bottom     #the denominator is on the bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def gcd(self, m, n):
        "Greatest Common Denominator"
        while m % n:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn

        return n

    def simplify(self):
        common = self.gcd(self.num, self.den)

        self.num /= common
        self.den /= common


    def __add__(self, fract):
        newnum = self.num * fract.den + self.den * fract.num
        newden = self.den * fract.den

        common = self.gcd(newnum, newden)

        return Fraction(newnum / common, newden / common)

    def __mul__(self, fract):
        newnum = self.num * fract.num
        newden = self.den * fract.den

        return Fraction(newnum, newden)

# //////////////////////////////////////////////////////////////////////////////
class Fraction(object):

    def __init__(self, top, bottom):
        self.num = top        #the numerator is on top
        self.den = bottom     #the denominator is on the bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def gcd(self, m, n):
        "Greatest Common Denominator"
        while m % n:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn

        return n

    def simplify(self):
        common = self.gcd(self.num, self.den)

        self.num /= common
        self.den /= common


    def __add__(self, fract):
        newnum = self.num * fract.den + self.den * fract.num
        newden = self.den * fract.den

        common = self.gcd(newnum, newden)

        return Fraction(newnum / common, newden / common)

    def __mul__(self, fract):
        newnum = self.num * fract.num
        newden = self.den * fract.den

        return Fraction(newnum, newden)

