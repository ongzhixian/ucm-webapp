import re
import unittest
from playwright.sync_api import sync_playwright, expect

class TestHome(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()
        cls.context = cls.browser.new_context()
        cls.page = cls.context.new_page()  # Use context to create the page

    @classmethod
    def tearDownClass(cls):
        
        cls.page.close()
        cls.context.close()
        cls.browser.close()
        cls.playwright.stop()

    def test_home_page_title_is_ucm(self):
        self.page.goto("https://ucm.readyperfectly.com")
        expect(self.page).to_have_title(re.compile("UCM"))
        self.page.screenshot(path=f"./screenshots/{self._testMethodName}.png")

if __name__ == "__main__":
    unittest.main()