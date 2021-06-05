'''
Разработайте конечный автомат из трех состояний и реализуйте его в виде взаимнорекурсивных функций.
'''

signals = 'rrbgrgb'


class Lamp:
    def __init__(self):
        self.state = None


def r(obj, signal, states):
    if signal == 'r':
        obj.state = signal
        change_state(obj, states)
    g(obj, signal, states)


def g(obj, signal, states):
    if signal == 'g':
        obj.state = signal
        change_state(obj, states)
    b(obj, signal, states)


def b(obj, signal, states):
    if signal == 'b':
        obj.state = signal
        change_state(obj, states)


def change_state(obj, states):
    if not len(states):
        return obj
    signal, states = states[0], states[1:]
    r(obj, signal, states)


change_state(Lamp(), signals)
