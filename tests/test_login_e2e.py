import pytest
import allure
from pages.login_page import LoginPage


@allure.epic("Hệ thống Văn phòng điện tử UTC")
@allure.feature("Xác thực & Đăng nhập")
class TestLoginUTC:

    @allure.story("Bảo mật giao diện")
    @allure.title("TC01: Kiểm tra ô mật khẩu ẩn ký tự (type='password')")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tc01_password_field_masked(self, driver):
        """Kiểm tra trường mật khẩu phải ở dạng ẩn ký tự để đảm bảo an toàn."""
        login_page = LoginPage(driver).open()
        assert login_page.get_password_input_type() == "password", (
            "Trường mật khẩu không được ẩn ký tự!"
        )

