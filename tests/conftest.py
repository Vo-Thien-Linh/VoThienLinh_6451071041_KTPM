import sys
import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Đảm bảo Python luôn tìm thấy thư mục gốc chứa 'base' và 'pages'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture(scope="function")
def driver(request):
    """Fixture khởi tạo trình duyệt Chrome trước mỗi test và đóng sau khi hoàn tất."""
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # Bỏ comment nếu muốn chạy ngầm
    
    _driver = webdriver.Chrome(service=service, options=options)
    yield _driver
    
    # Chụp ảnh màn hình đính kèm Allure nếu test thất bại
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            allure.attach(
                _driver.get_screenshot_as_png(),
                name="Screenshot_Error",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception:
            pass

    _driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook ghi nhận kết quả test để phục vụ việc chụp ảnh màn hình khi có lỗi."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
