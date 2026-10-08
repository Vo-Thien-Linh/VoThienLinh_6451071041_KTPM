import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """Fixture khởi tạo trình duyệt Chrome trước mỗi test và đóng sau khi hoàn tất.
    Tương đương BaseTest trong JUnit/TestNG.
    """
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # Bỏ comment nếu muốn chạy ngầm
    
    _driver = webdriver.Chrome(service=service, options=options)
    yield _driver
    _driver.quit()
