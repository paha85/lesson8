def type_logger(func):
    def type_blogger(*args, **kwargs):
        for arg in args:
            print(f'{func.__name__} ({arg}: cube = {func(arg)} {type(func(arg))})', end=', ')
        for k, v in kwargs.items():
            print(f'{func.__name__} ({k} = {v}: cube = {func(v)} {type(func(v))})', end=', ')

    return type_blogger


@type_logger
def calc_cube(*args):
    for arg in args:
        return arg ** 3


calc_cube(4, 6, 8, 5, f=4)
