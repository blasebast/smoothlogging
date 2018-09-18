import glob
import pytest
import re
import unittest
from smoothlogging.smoothlogging import smoothlogging

lobj = smoothlogging()
log_root_name = "testlog"
rex = re.compile("%s_\d+\.log" % (log_root_name))
log = lobj.log(".",log_root_name)

class TestLoggingModule(unittest.TestCase):

    def test_info(self):
        self.assertIsNone(log.info("log info"))

    def test_warning(self):
        self.assertIsNone(log.info("log_warning"))

    def test_error(self):
        self.assertIsNone(log.info("log error"))

    def test_file_created(self):
        self.rex = re.compile("testlog_\d+\.log")
        self.number_of_log_files = glob.glob("./%s_*" % (log_root_name)).__len__()
        self.assertGreaterEqual(self.number_of_log_files, 1)

@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string



if __name__ == '__main__':
    unittest.main()

