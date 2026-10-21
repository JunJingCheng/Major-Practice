import unittest
from utils.fetch_bcw_dataset import fetch_local_bcw
from scikit_roughsets.roughsets import RoughSetsReducer
import numpy as np


class TestRoughSetsReducer(unittest.TestCase):
    def test_reduce(self):
        U = fetch_local_bcw()
        reducer = RoughSetsReducer()
        X = U[U.columns[0:-1]].to_numpy()
        y = np.array([U[U.columns[-1]]]).T
        self.assertEqual(
            ['Clump_thickness', 'Uniformity_of_cell_shape', 'Single_epithelial_cell_size', 'Bare_nuclei'],
            list(U.columns[reducer.reduce(X, y).astype('int64')-1])
        )


if __name__ == "__main__":
    unittest.main()