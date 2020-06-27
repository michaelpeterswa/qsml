import unittest
import qsml


class TestDump(unittest.TestCase):
    def test_dump_groupname(self):
        file = "tests/dump.qsml"
        string_val = "13"
        int_val = 6
        returned_val = {int_val: {"GOOG": 4, "AAPL": 5, "BRK.B": 1}}
        with self.assertRaises(qsml.dumperror.QSMLDumpError):
            qsml.dump("dumptest.qsml", returned_val)

    def test_dump_stockname(self):
        file = "tests/dump.qsml"
        string_val = "13"
        int_val = 6
        returned_val = {"myportfolio": {int_val: 4, "AAPL": 5, "BRK.B": 1}}
        with self.assertRaises(qsml.dumperror.QSMLDumpError):
            qsml.dump("dumptest.qsml", returned_val)

    def test_dump_value(self):
        file = "tests/dump.qsml"
        string_val = "13"
        returned_val = {"myportfolio": {"GOOG": string_val, "AAPL": 5, "BRK.B": 1}}
        with self.assertRaises(qsml.dumperror.QSMLDumpError):
            qsml.dump("dumptest.qsml", returned_val)


if __name__ == "__main__":
    unittest.main()
