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

    @allure.story("Tương tác giao diện")
    @allure.title("TC02: Kiểm tra toggle checkbox 'Giữ tôi luôn đăng nhập'")
    @allure.severity(allure.severity_level.MINOR)
    def test_tc02_remember_me_toggle(self, driver):
        """Kiểm tra tương tác bật/tắt checkbox lưu phiên đăng nhập."""
        login_page = LoginPage(driver).open()
        initial_state = login_page.is_remember_me_selected()

        login_page.toggle_remember_me()
        assert login_page.is_remember_me_selected() != initial_state, (
            "Trạng thái checkbox không thay đổi sau khi click!"
        )

