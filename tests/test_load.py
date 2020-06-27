import unittest
import qsml


class TestLoad(unittest.TestCase):
    def test_load(self):
        file = "tests/load.qsml"
        returned_val = {
            "myportfolio": {"GOOG": 10, "AAPL": 5, "BRK.B": 1},
            "test": {"SNAP": 130, "MSFT": 5, "TSLA": 100},
        }
        self.assertEqual(qsml.load(file), returned_val, "Were not equal")

    def test_load_comment_error(self):
        file = "tests/load2.qsml"
        with self.assertRaises(qsml.error.QSMLError):
            qsml.load(file)


if __name__ == "__main__":
    unittest.main()
