class Complex:
    def __init__(self, real, imag):
        self.real = real          # real part
        self.imag = imag          # imaginary part

    def __add__(self, other):
        """Overload + operator: (a + bi) + (c + di) = (a+c) + (b+d)i"""
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __mul__(self, other):
        """Overload * operator: (a + bi)(c + di) = (ac − bd) + (ad + bc)i"""
        real_part = (self.real * other.real) - (self.imag * other.imag)
        imag_part = (self.real * other.imag) + (self.imag * other.real)
        return Complex(real_part, imag_part)

    def __str__(self):
        """Readable format when printing the object"""
        return f"{self.real} + {self.imag}i"


# Example usage:
c1 = Complex(3, 2)
c2 = Complex(1, 7)

print("c1 =", c1)
print("c2 =", c2)

print("Addition:", c1 + c2)        # Calls __add__
print("Multiplication:", c1 * c2)  # Calls __mul__
