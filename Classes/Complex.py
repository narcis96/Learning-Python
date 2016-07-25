import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)

    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real, imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imaginary)

    def __div__(self, no):
        x = float(no.real ** 2 + no.imaginary ** 2)
        y = self * Complex(no.real, -no.imaginary)
        real = y.real / x
        imaginary = y.imaginary / x
        return Complex(real, imaginary)

    def mod(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "%.2fi" % (self.imaginary)
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


C = map(float, raw_input("x = ").split())
D = map(float, raw_input("y = ").split())
x = Complex(*C)
y = Complex(*D)
print 'x + y =', x + y
print 'x - y =', x - y
print 'x * y =', x * y
print 'x / y =', x / y
print '|x| = ', x.mod()
print '|y| = ', y.mod()
