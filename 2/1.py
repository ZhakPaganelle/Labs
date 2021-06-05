'''
Создайте два варианта функции, которая возвращает кортеж значений. Первый вариант
принимает на вход параметры в виде кортежа, второй вариант параметры в каррированном виде.
'''


def tuple_in_out_1(tup):
    '''
    Returns doubled values of input tuple
    '''
    tup = (i*2 for i in tup)
    return tuple(tup)


def doubling_vector(x):
    '''
    Returns tuple of doubled values of all arguments
    '''
    def double_y(y):
        def double_z(z):
            return (2*x, 2*y, 2*z)
        return double_z
    return double_y
