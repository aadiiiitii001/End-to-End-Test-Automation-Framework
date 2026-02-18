from pages.base_page import BasePage

class DashboardPage(BasePage):
    HEADER = "h1"

    def get_header_text(self):
        return self.get_text(self.HEADER)
