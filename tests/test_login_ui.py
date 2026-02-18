from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import Config

def test_valid_login(page):
    page.goto(f"{Config.BASE_URL}/login")

    login_page = LoginPage(page)
    login_page.login("testuser", "password123")

    dashboard = DashboardPage(page)
    assert "Dashboard" in dashboard.get_header_text()
