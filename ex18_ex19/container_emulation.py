import re


def key_to_format(key):
    if len(key) > 1:
        str_key = [str(element).lower() for element in key]
        if str_key[0].isdigit():
            str_key = str_key[::-1]
        return "".join(str_key)
    else:
        if key[0][0].isdigit():
            key = key[0][::-1]
            print(key)
        return "".join(key)


def reg_exp_check(key):
    key = key_to_format(key)  # переводим ключ в формат нужного вида
    pattern = r'^[A-Za-z]\d+$'
    if not re.match(pattern, key):  # проверяем на правильность ввода
        return False
    return True


class Field(dict):
    def __getitem__(self, key):
        if type(key) is not tuple:
            if type(key) is not str:
                raise TypeError(f"Неправильный тип данных ключа! Введённый тип: {type(key)}")
        if not reg_exp_check(key):
            raise ValueError
        return super(Field, self).__getitem__(key_to_format(key))

    def __setitem__(self, key, value):
        if type(key) is not tuple:
            if type(key) is not str:
                raise TypeError(f"Неправильный тип данных ключа! Введённый тип: {type(key)}")
        if not reg_exp_check(key):
            raise ValueError
        return super(Field, self).__setitem__(key_to_format(key), value)

    def __delitem__(self, key):
        return super(Field, self).__delitem__(key_to_format(key))

    def __missing__(self, key):
        return None

    def __contains__(self, item):
        return self[item] != self.__missing__(1)

    def __iter__(self):
        return iter(self.values())  # Возвращаем итератор значений

    def __next__(self):
        # Возвращаем следующий ключ и его значение
        key = next(iter(self.keys()))
        value = self[key]
        return key, value

    def __setattr__(self, key, value):
        try:
            return self.__setitem__(key, value)
        except:
            self.__dict__[key] = value

    def __getattr__(self, item):
        if reg_exp_check(item):
            return self.__getitem__(item)

    def __delattr__(self, item):
        try:
            return self.__delitem__(item)
        except:
            del self.__dict__[item]


field = Field()
field[(1, 'A')] = 25
field[1, 'v'] = 60
field[1, 'b'] = 100
field['2c'] = 2
field.D4 = 11
print(field.__dict__)
del field.d4
print(field.D4)
field.abcde = 125
print(field.__dict__)
del field.abcde
print(field.abcde)
