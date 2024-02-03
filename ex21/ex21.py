import time


def time_decorator(func):
    def wrapper():
        start = time.time()
        res = func()
        finish = time.time()
        print(int(finish - start))
        return res
    return wrapper


@time_decorator
def sleep_1_sec():
    time.sleep(1.25)
    print("function")
    return 25


result = sleep_1_sec()

print(result)
