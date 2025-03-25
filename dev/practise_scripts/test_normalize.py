import pytest
import numpy as np

def normalize(X):
    return (X - X.min())/(X.max() - X.min())

@pytest.fixture(params=[(1,1),(2,2),(3,3),(4,4)], ids=lambda d: f"rows: {d}")
def random_numpy_array(request):
    return np.random.normal(request.param)

def test_shape_same(random_numpy_array):
    X_norm = normalize(random_numpy_array)
    assert X_norm.min() == 0.0
    assert X_norm.max() == 1.0
