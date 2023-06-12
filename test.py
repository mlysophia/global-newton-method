from global_newton_method import FindMinimum
from configuration import delta0


def test():
    example = FindMinimum()
    try:
        example.global_newton_method(delta0)
    except TypeError:
        print('The expression entered must be a function with one variant x!')


test()
