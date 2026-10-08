from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Lớp cha đại diện cho trang cơ sở, chứa WebDriver và các hàm tiện ích dùng chung."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_url(self, url):
        """Mở một địa chỉ URL."""
        self.driver.get(url)

    def find(self, locator):
        """Tìm và chờ phần tử hiển thị trên trang."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_present(self, locator):
        """Tìm phần tử có mặt trong DOM (kể cả khi bị ẩn)."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Chờ phần tử có thể click được và thực hiện click."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text, clear_first=True):
        """Nhập dữ liệu vào ô input."""
        element = self.find(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Lấy nội dung văn bản của phần tử."""
        return self.find(locator).text

    def get_attribute(self, locator, attribute_name):
        """Lấy giá trị thuộc tính HTML của phần tử."""
        return self.find_present(locator).get_attribute(attribute_name)

    def is_displayed(self, locator):
        """Kiểm tra phần tử có đang hiển thị không."""
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def wait_for_url_contains(self, text):
        """Chờ URL hiện tại chứa đoạn text mong muốn."""
        return self.wait.until(EC.url_contains(text))

    def wait_for_url_changes(self, current_url):
        """Chờ URL hiện tại thay đổi."""
        return self.wait.until(EC.url_changes(current_url))

    def get_current_url(self):
        """Lấy URL hiện tại của trình duyệt."""
        return self.driver.current_url
