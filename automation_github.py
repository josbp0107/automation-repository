from selenium import webdriver
import getpass


class AutomationGitHub(object):

    def __init__(self, driver):
        self._driver = driver
        self._url = 'https://github.com/'
        self.sign_in = 'Sign in'

    def open(self):
        self._driver.get(self._url)
        self._driver.maximize_window()
        self._driver.find_element_by_link_text(self.sign_in).click()

    def get_user(self):
        driver = self._driver

        user_name = input('Username: ')
        password = getpass.getpass('Password: ')

        field_login = driver.find_element_by_xpath('//*[@id="login_field"]')
        field_login.send_keys(user_name)

        field_pass = driver.find_element_by_xpath('//*[@id="password"]')
        field_pass.send_keys(password)

        submit_button = driver.find_element_by_name('commit')
        submit_button.click()