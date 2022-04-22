def type_logger(func):
    def type_blogger(*args):
        for arg in args:
            print(f'{func.__name__} ({arg}: cube = {func(arg)} {type(func(arg))})', end=', ')
    return type_blogger


@type_logger
def calc_cube(*args):
    for arg in args:
        return arg ** 3


calc_cube(4, 6, 8, 5, 3)
