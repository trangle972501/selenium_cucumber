from webportal.support.browsers import BrowserName
from webportal.browser.chrome import ChromeDriver
from webportal.browser.firefox import FirefoxDriver
from webportal.browser.edge import EdgeDriver


class DriverManager:
    _browser_manager = None

    def __init__(self):
        self._browser_manager = {
            BrowserName.CHROME: self._start_chrome,
            BrowserName.FIREFOX: self._start_firefox,
            BrowserName.EDGE: self._start_edge
        }

    def start_driver(self, name, capabilities):
        return self._browser_manager[name](capabilities)

    def _start_chrome(self, capabilities):
        print(capabilities)
        return ChromeDriver().create_driver(capabilities)

    def _start_firefox(self, capabilities):
        return FirefoxDriver().create_driver(capabilities)

    def _start_edge(self, capabilities):
        return EdgeDriver().create_driver(capabilities)
