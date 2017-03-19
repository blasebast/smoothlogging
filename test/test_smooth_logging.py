import unittest
from sebmodules.smoothlogging import smoothlogging

lobj = smoothlogging()
log = lobj.log("c:/temp","testlog")

class TestLoggingModule(unittest.TestCase):

    def test_info(self):
        self.assertIsNone(log.info("log info"))

    def test_warning(self):
        self.assertIsNone(log.info("log_warning"))

    def test_error(self):
        self.assertIsNone(log.info("log error"))

if __name__ == '__main__':
    unittest.main()
