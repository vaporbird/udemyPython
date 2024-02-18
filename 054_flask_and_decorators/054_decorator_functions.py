import time
current_time = time.time()
print(current_time)


def speed_calc_decorator(*args, **kwargs):
    def wrapper(func):
        global current_time
        func()
        print(kwargs["desc_msg"] + ": ", time.time() - current_time)
        current_time = time.time()

    return wrapper


@speed_calc_decorator(desc_msg="fast")
def fast_function():
    for i in range(1000000):
        i*i


@speed_calc_decorator(desc_msg="slow")
def slow_function():
    for i in range(10000000):
        i*i


#fast_function()
#slow_function()
