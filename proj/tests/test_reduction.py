import unittest
from src.reduction import RoughSetsReducer


class TestReduction(unittest.TestCase):
    
    reducer = RoughSetsReducer()
    
    def test_equiv_cls(self):
        raise NotImplementedError()

    def test_under_appr(self):
        raise NotImplementedError()

    def test_pos(self):
        raise NotImplementedError()

    def test_gamma(self):
        self.assertEqual(1.0,
            self.reducer.gamma(
                ['Clump_thickness', 'Uniformity_of_cell_shape', 
                'Single_epithelial_cell_size', 'Bare_nuclei']
            )
        )

    def test_core(self):
        raise NotImplementedError()

    def test_reduce(self):
        raise NotImplementedError()


if __name__ == "__main__":
    unittest.main()