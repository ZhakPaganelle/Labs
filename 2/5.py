'''
Разработайте функцию, которая принимает 3 целых числа и лямбда-выражение для их
суммирования в виде кортежа и в каррированном виде.
'''

from functools import partial


def count(*args):
    if not callable(args[-1]):
        return partial(count, *args)

    return args[-1](args[:-1])


# Tuple sum
print(count((1, 2, 3), lambda arr: sum(arr[0])))

# Carrying
print(count(1)(2)(3)(lambda arr: sum(arr)))
