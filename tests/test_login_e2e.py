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

    @allure.story("Kiểm tra Validation")
    @allure.title("TC04: Nhập Tên đăng nhập nhưng để trống Mật khẩu")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc04_login_empty_password(self, driver):
        """Hệ thống phải yêu cầu nhập mật khẩu khi chỉ có tên đăng nhập."""
        login_page = LoginPage(driver).open()
        login_page.login(username="sinhvien_utc", password="")

        error_text = login_page.get_error_message()
        assert "chưa nhập mật khẩu" in error_text.lower(), (
            f"Thông báo lỗi không đúng: {error_text}"
        )

    @allure.story("Kiểm tra Validation")
    @allure.title("TC05: Để trống Tên đăng nhập nhưng có nhập Mật khẩu")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc05_login_empty_username(self, driver):
        """Hệ thống phải yêu cầu nhập tên đăng nhập khi chỉ có mật khẩu."""
        login_page = LoginPage(driver).open()
        login_page.login(username="", password="MatKhau123@")

        error_text = login_page.get_error_message()
        assert "chưa nhập tên đăng nhập" in error_text.lower(), (
            f"Thông báo lỗi không đúng: {error_text}"
        )

    @allure.story("Xác thực thông tin")
    @allure.title("TC06: Đăng nhập với tài khoản hoặc mật khẩu không chính xác")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tc06_login_invalid_credentials(self, driver):
        """Hệ thống từ chối đăng nhập với thông tin không đúng."""
        login_page = LoginPage(driver).open()
        login_page.login(username="sinhvien_utc_invalid", password="MatKhauSai@999")

        error_text = login_page.get_error_message()
        assert "tài khoản hoặc mật khẩu không đúng" in error_text.lower(), (
            f"Thông báo lỗi không đúng: {error_text}"
        )

    @allure.story("Điều hướng liên kết")
    @allure.title("TC07: Kiểm tra liên kết 'Bạn quên mật khẩu đăng nhập ?'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc07_navigate_to_forgot_password(self, driver):
        """Kiểm tra điều hướng sang trang cấp lại mật khẩu (/Login/GetPass)."""
        login_page = LoginPage(driver).open()
        login_page.click_forgot_password()

        login_page.wait_for_url_contains("GetPass")
        current_url = login_page.get_current_url()
        assert "getpass" in current_url.lower(), f"URL chuyển hướng sai: {current_url}"

    @allure.story("Cổng xác thực SSO")
    @allure.title("TC08: Kiểm tra điều hướng nút 'Đăng nhập bằng e-mail UTC'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tc08_click_sso_utc_email(self, driver):
        """Kiểm tra chuyển hướng sang trang Google OAuth khi đăng nhập bằng mail trường."""
        login_page = LoginPage(driver).open()
        login_page.click_utc_email_sso()

        login_page.wait_for_url_contains("accounts.google.com")
        current_url = login_page.get_current_url()
        assert "accounts.google.com" in current_url.lower(), (
            f"Không chuyển sang trang SSO Google: {current_url}"
        )

    @pytest.mark.skip(reason="Cần cung cấp tài khoản và mật khẩu UTC thực tế để chạy case này")
    @allure.story("Đăng nhập thành công")
    @allure.title("TC09: Đăng nhập thành công với tài khoản hợp lệ (Happy Path)")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_tc09_login_success(self, driver):
        """Kiểm tra luồng đăng nhập chính xác đưa người dùng vào hệ thống."""
        login_page = LoginPage(driver).open()
        VALID_USER = "dien_tai_khoan_that_o_day"
        VALID_PASS = "dien_mat_khau_that_o_day"

        login_page.login(username=VALID_USER, password=VALID_PASS)
        login_page.wait_for_url_changes(login_page.URL)
        assert "/Login" not in login_page.get_current_url()

