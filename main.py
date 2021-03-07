import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from automation_github import AutomationGitHub


class MainTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')

    def test_sign_in(self):
        github = AutomationGitHub(self.driver)
        github.open()
        github.get_user()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='github_report'))
