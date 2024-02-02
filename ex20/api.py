def register_booking(booking):
    i = int(input())
    if i == 1:
        return True
    elif i == 2:
        return False
    else:
        raise KeyError
