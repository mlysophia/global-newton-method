import sympy
from sympy.abc import x
from configuration import max_iteration_step, epi


# get user's input
def get_input(func=''):

    print('Welcome! This program helps you find a local minimum for a function with one variable x. '
          'Enter the function you want to test: ')
    try:
        func = sympy.sympify(input())
    except Exception as error:
        print(str(error))
    print('Enter a start point you like: ')
    start = eval(input())

    return func, start


class FindMinimum:

    # initialize
    def __init__(self):
        self.func, self.start = get_input()
        self.diff1 = sympy.diff(self.func)
        self.diff2 = sympy.diff(self.diff1)

    # optimize
    def global_newton_method(self, step_length):

        count = 0
        ite = self.start

        while count < max_iteration_step:

            d1 = self.diff1.subs(x, ite)
            d2 = self.diff2.subs(x, ite)
            if abs(d1) <= epi and d2 >= 0:
                break
            elif abs(d1) <= epi and d2 < 0:
                delta1 = step_length
                while self.func.subs(x, ite + delta1) < self.func.subs(x, ite):
                    delta1 = delta1/2
                ite = ite + delta1
                count = count + 1
                continue
            else:
                alpha1 = 1
                if d2 > 0:
                    beta1 = d2
                else:
                    beta1 = 1
                while self.func.subs(x, ite - alpha1*d1/beta1) > (self.func.subs(x, ite) - alpha1*d1**2/4/beta1):
                    alpha1 = alpha1/4
                ite = ite - alpha1*d1/beta1
                count = count + 1
                continue

        if count < max_iteration_step:
            print('test function:', self.func, '\nlocal minimum: f(%.4f)=%.4f' % (ite, self.func.subs(x, ite)))
        else:
            print('Exceed the maximal iteration steps!')
