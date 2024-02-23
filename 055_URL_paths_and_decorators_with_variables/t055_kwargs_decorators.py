def show_func_dec(func):
    def wrapper(*args, **kwargs):
        print("Called function: "
              f"{func.__name__}({args[0]}, {args[1]}, {args[2]})")
        func(args[0], args[1], args[2])
    return wrapper


def show_func_res_dec(func):
    def wrapper(*args, **kwargs):
        result = func(args[0], args[1], args[2])
        print("Result:", result)
    return wrapper


@show_func_dec
@show_func_res_dec
def a_function(a: int, b: int, c: int):
    return a*b*c


a_function(2, 3, 4)
a_function(5, 6, 7)
a_function(7, 9, 8)
