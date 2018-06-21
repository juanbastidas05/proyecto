import unittest
import pandas as pd
import numpy as np

class MyTestCase(unittest.TestCase):
    def test_something(self):
     t = pd.Series([1, 3, 5, np.nan, 6, 8])
     df = pd.read_csv('.././base/test.csv')
     print(df)

if __name__ == '__main__':
    unittest.main()