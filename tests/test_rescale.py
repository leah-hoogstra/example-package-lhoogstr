import numpy as np
from example_package_lhoogstr.rescale import rescale

# to use pytest, it's important that this file has the prefix "test_" and that the test functions also have the prefix "test_"
def test_rescale():
   np.testing.assert_allclose(
   rescale(np.linspace(0, 100, 5)),
   np.array([0.0, 0.25, 0.5, 0.75, 1.0]),
   )
