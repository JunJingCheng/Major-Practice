import unittest


class TestDiscretization(unittest.TestCase):
    def test_foolish_discretization(self):
        from src.preprocessing import fetch_nona_bcw, foolish_discretization
        original = fetch_nona_bcw()['Bare_nuclei']
        discretized = foolish_discretization(original=original)
        self.assertListEqual(
            discretized.tolist(),
            discretized.copy().astype("int64").tolist()
        )
        

if __name__ == "__main__":
    unittest.main()