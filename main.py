__author__ = 'gillianseed'

def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

class Polynom:

    def __init__(self, coeffs):
        self._coeffs = coeffs[:]
        while self._coeffs and self._coeffs[-1] == 0:
            del self._coeffs[-1]

        if not self._coeffs:
            self._coeffs = [0]
            self._deg = float('-inf')
        else:
            self._deg = len(self._coeffs) - 1

    def __getitem__(self, item):
        return self._coeffs[item] if item >= 0 and item <=self.deg() else 0

    def __len__(self):
        return len(self._coeffs)

    def deg(self):
        return self._deg

    def __pow__(self, power, modulo=None):
        if power == 0:
            return Polynom([1])
        else:
            res = self
            for i in range(power-1):
                res = res * self
            return res

    def __add__(self, other):
        if type(other) in [float, int]:
            return self.__add__(Polynom([other]))
        else:
            return Polynom([self[i]+other[i] for i in range(max(self.deg(), other.deg())+1)])

    def __neg__(self):
        return Polynom([-x for x in self])

    def __sub__(self, other):
        return Polynom([self[i]-other[i] for i in range(max(self.deg(), other.deg())+1)])

    def __mul__(self, other):
        return Polynom([sum(self[i]*other[k-i] for i in range(k+1)) for k in range(self.deg()+other.deg()+1)])

    def __rmul__(self, other):
        return Polynom([x * other for x in self._coeffs])

    def __repr__(self):
        return 'Polynom(%s)' % self._coeffs

    def derivate(self):
        return Polynom([self[i] * i for i in range(1, self.deg()+1)])

    def __call__(self, value):
        return sum(coeff * value ** i for i, coeff in enumerate(self._coeffs))

    def __radd__(self, other):
        return self if other == 0 else self+other


X = Polynom([0, 1])
P = 5*X**3-X**2-3*X+2

lst = [P]

while lst[-1].deg():
    lst.append(lst[-1].derivate())

Q = sum(pol(0)/factorial(i)*X**i for (i,pol) in enumerate(lst))

print(P,Q)

