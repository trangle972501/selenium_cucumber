from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class EdgeDriver():

    def create_driver(self, capabilities):
        options = webdriver.EdgeOptions()
        return webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(), options=options, capabilities=capabilities)
