import numpy as np
import pytest
import sys
sys.path.append("../ODE_Solver/ODE_Solver")

from ODE_Solver import Update_vars

def test_update_vars():

    func = lambda x, y ,z : np.sin(x)/x + 1/(y- 0.75)/(z - 3.5) 

    test_x = np.linspace(-10, 10, 101)
    test_y = np.linspace(-65.25, 9.75, 101)
    test_z = np.linspace(-30.25, 44.75, 101)
    h = 0.001
     
    x, y, z = Update_vars(func, h,test_x, test_y, test_z)

    assert not np.isnan(x).any()
    assert not np.isnan(y).any()
    assert not np.isnan(z).any()

if __name__ == '__main__':
    test_update_vars()