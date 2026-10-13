from unittest import TestCase


class TestFetchBcw(TestCase):
    def test_fetch_bcw_dataset(self):
        from utils.fetch_bcw_dataset import fetch_local_bcw
        import pandas as pd
        bcw_df = fetch_local_bcw()
        self.assertIsInstance(bcw_df, pd.DataFrame)
        self.assertFalse(bcw_df.empty)


if __name__ == "__main__":
    unittest.main()