class BaseWallet:
    exchange_rate = 1

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, BaseWallet):
            new_amount = self.amount + (other.amount * other.exchange_rate / self.exchange_rate)
        else:
            # а если второй объект не этого класса, то попробуем его привести к типу float
            new_amount = self.amount + float(other)
        return self.__class__(self.name, new_amount)

    def __iadd__(self, other):
        if isinstance(other, BaseWallet):
            new_amount = self.amount + (other.amount * other.exchange_rate / self.exchange_rate)
        else:
            # а если второй объект не этого класса, то попробуем его привести к типу float
            new_amount = self.amount + float(other)
        return self.__class__(self.name, new_amount)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, BaseWallet):
            new_amount = self.amount - (other.amount * other.exchange_rate / self.exchange_rate)
        else:
            # а если второй объект не этого класса, то попробуем его привести к типу float
            new_amount = self.amount - float(other)
        return self.__class__(self.name, new_amount)

    def __isub__(self, other):
        if isinstance(other, BaseWallet):
            new_amount = self.amount - (other.amount * other.exchange_rate / self.exchange_rate)
        else:
            # а если второй объект не этого класса, то попробуем его привести к типу float
            new_amount = self.amount - float(other)
        return self.__class__(self.name, new_amount)

    def __rsub__(self, other):

        new_amount = float(other) - self.amount
        return self.__class__(self.name, new_amount)

    def __mul__(self, other):
        # а если второй объект не этого класса, то попробуем его привести к типу float
        new_amount = self.amount * float(other)
        return self.__class__(self.name, new_amount)

    def __imul__(self, other):
        # а если второй объект не этого класса, то попробуем его привести к типу float
        new_amount = self.amount * float(other)
        return self.__class__(self.name, new_amount)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        # а если второй объект не этого класса, то попробуем его привести к типу float
        new_amount = self.amount / float(other)
        return self.__class__(self.name, new_amount)

    def __itruediv__(self, other):
        # а если второй объект не этого класса, то попробуем его привести к типу float
        new_amount = self.amount / float(other)
        return self.__class__(self.name, new_amount)

    def __rdiv__(self, other):
        return self.__truediv__(other)

    def __eq__(self, other):
        if isinstance(other, BaseWallet):
            if self.amount == (other.amount * other.exchange_rate / self.exchange_rate):
                return True
            return False

    def spend_all(self):
        if self.amount > 0:
            self.amount = 0

    def to_base(self):
        return self.amount * self.exchange_rate


class RubbleWallet(BaseWallet):
    exchange_rate = 1

    def __str__(self):
        return f"""Rubble Wallet {self.name} {self.amount}"""


class DollarWallet(BaseWallet):
    exchange_rate = 60

    def __str__(self):
        return f"""Dollar Wallet {self.name} {self.amount}"""


class EuroWallet(BaseWallet):
    exchange_rate = 70

    def __str__(self):
        return f"""Euro Wallet {self.name} {self.amount}"""


a = RubbleWallet('rub1', 15)
a = 10 - a
b = RubbleWallet('rub2', 20)
c = a + b
print(a, b, c, sep='\n')