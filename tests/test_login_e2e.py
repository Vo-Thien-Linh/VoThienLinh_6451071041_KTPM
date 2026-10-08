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

    @allure.story("Kiểm tra Validation")
    @allure.title("TC03: Bấm Đăng nhập khi để trống cả 2 trường")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc03_login_empty_both_fields(self, driver):
        """Hệ thống phải cảnh báo khi không nhập bất kỳ thông tin nào."""
        login_page = LoginPage(driver).open()
        login_page.click_login_button()

        error_text = login_page.get_error_message()
        assert "chưa nhập tên đăng nhập" in error_text.lower(), (
            f"Thông báo lỗi không đúng: {error_text}"
        )

