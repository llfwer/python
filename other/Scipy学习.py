import numpy as np
from scipy.optimize import optimize


def f(x):
    return x ** 2 + 10 * np.sin(x)


# BFGS优化算法求复杂曲线最小值
def l_bfgs_min():
    print(optimize.fmin_bfgs(f, 0))


l_bfgs_min()
