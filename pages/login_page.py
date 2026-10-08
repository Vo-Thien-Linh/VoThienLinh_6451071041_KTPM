from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginPage(BasePage):
    """Page Object đại diện cho trang Đăng nhập Văn phòng điện tử UTC.
    Chứa toàn bộ Locators và Actions của trang.
    """

    URL = "https://vanphongdientu.utc.edu.vn/Login"

    # --- Locators ---
    LOC_USERNAME = (By.NAME, "username")
    LOC_PASSWORD = (By.NAME, "userpwd")
    LOC_REMEMBER_INPUT = (By.ID, "persistent")
    LOC_REMEMBER_LABEL = (By.CSS_SELECTOR, "label.check, label[for='persistent']")
    LOC_BTN_LOGIN = (By.CSS_SELECTOR, "input.submit_login[type='submit']")
    LOC_BTN_UTC_EMAIL = (By.XPATH, "//a[contains(text(), 'Đăng nhập bằng e-mail UTC')]")
    LOC_FORGOT_PW = (By.XPATH, "//a[contains(@href, '/Login/GetPass')]")
    LOC_ERROR_MSG = (By.CSS_SELECTOR, "div.error")
    LOC_CAPTCHA_IMG = (By.ID, "captcha")
    LOC_CAPTCHA_INPUT = (By.NAME, "captcha")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        """Mở trang đăng nhập UTC."""
        self.open_url(self.URL)
        return self

    def enter_username(self, username):
        """Nhập tên đăng nhập."""
        self.enter_text(self.LOC_USERNAME, username)
        return self

    def enter_password(self, password):
        """Nhập mật khẩu."""
        self.enter_text(self.LOC_PASSWORD, password)
        return self

    def click_login_button(self):
        """Nhấn nút Đăng nhập."""
        self.click(self.LOC_BTN_LOGIN)
        return self

    def login(self, username, password):
        """Hành động đăng nhập hoàn chỉnh với username và password."""
        if username:
            self.enter_username(username)
        if password:
            self.enter_password(password)
        self.click_login_button()
        return self

    def toggle_remember_me(self):
        """Click vào nhãn checkbox 'Giữ tôi luôn đăng nhập'."""
        self.click(self.LOC_REMEMBER_LABEL)
        return self

    def is_remember_me_selected(self):
        """Kiểm tra trạng thái được chọn của checkbox."""
        checkbox = self.find_present(self.LOC_REMEMBER_INPUT)
        return checkbox.is_selected()

    def click_forgot_password(self):
        """Nhấn vào liên kết 'Bạn quên mật khẩu đăng nhập ?'."""
        self.click(self.LOC_FORGOT_PW)
        return self

    def click_utc_email_sso(self):
        """Nhấn vào nút 'Đăng nhập bằng e-mail UTC'."""
        self.click(self.LOC_BTN_UTC_EMAIL)
        return self

    def get_password_input_type(self):
        """Lấy giá trị thuộc tính type của ô Mật khẩu."""
        return self.get_attribute(self.LOC_PASSWORD, "type")

    def get_error_message(self):
        """Lấy nội dung thông báo lỗi trên form."""
        return self.get_text(self.LOC_ERROR_MSG)

    def is_error_displayed(self):
        """Kiểm tra thông báo lỗi có hiển thị không."""
        return self.is_displayed(self.LOC_ERROR_MSG)

    def is_captcha_displayed(self):
        """Kiểm tra hình ảnh mã bảo mật (Captcha) có xuất hiện không."""
        return self.is_displayed(self.LOC_CAPTCHA_IMG)

    def is_captcha_input_displayed(self):
        """Kiểm tra ô nhập mã bảo mật Captcha có xuất hiện không."""
        return self.is_displayed(self.LOC_CAPTCHA_INPUT)
