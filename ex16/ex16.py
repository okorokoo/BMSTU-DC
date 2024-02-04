class Calculator:

    last = None

    def __init__(self):
        self.hist = []

    def sum(self, a, b):
        # Calculator.hist.insert(0, f'''sum({a}, {b}) == {a + b}''')
        Calculator.last = f'''sum({a}, {b}) == {a + b}'''
        self.hist.insert(0, f'''sum({a}, {b}) == {a + b}''')
        return a + b

    def sub(self, a, b):
        # Calculator.hist.insert(0, f'''sub({a}, {b}) == {a - b}''')
        Calculator.last = f'''sub({a}, {b}) == {a - b}'''
        self.hist.insert(0, f'''sub({a}, {b}) == {a - b}''')
        return a - b

    def mul(self, a, b):
        # Calculator.hist.insert(0, f'''mul({a}, {b}) == {a * b}''')
        Calculator.last = f'''mul({a}, {b}) == {a * b}'''
        self.hist.insert(0, f'''mul({a}, {b}) == {a * b}''')
        return a * b

    def div(self, a, b, mod=False):
        if mod:
            Calculator.last = f'''div({a}, {b}) == {a % b}'''
            self.hist.insert(0, f'''div({a}, {b}) == {a % b}''')
            return a % b
        Calculator.last = f'''div({a}, {b}) == {a / b}'''
        self.hist.insert(0, f'''div({a}, {b}) == {a / b}''')
        return a / b

    def history(self, n):
        if self.hist:
            return self.hist[n-1]

    @classmethod
    def clear(cls):
        cls.last = None