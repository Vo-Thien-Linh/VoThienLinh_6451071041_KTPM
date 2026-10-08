# 🚀 AUTOMATION TESTING E2E - HỆ THỐNG VĂN PHÒNG ĐIỆN TỬ UTC

> **Đồ án / Bài tập thực hành môn Kiểm thử phần mềm (KTPM)**  
> **Sinh viên thực hiện:** Võ Thiên Lĩnh  
> **Mã số sinh viên (MSSV):** 6451071041  
> **Trường đại học:** Trường Đại học Giao thông Vận tải (UTC)  
> **Hệ thống kiểm thử (AUT):** [https://vanphongdientu.utc.edu.vn/Login](https://vanphongdientu.utc.edu.vn/Login)  

---

## 📌 1. Giới thiệu tổng quan

Dự án này là bộ kiểm thử tự động toàn diện (End-to-End Automation Testing) dành cho màn hình Xác thực & Đăng nhập của cổng thông tin **Văn phòng điện tử UTC**.

### Điểm nổi bật của dự án:
- **Kiến trúc chuẩn công nghiệp:** Xây dựng theo mô hình **Page Object Model (POM)** tách biệt hoàn toàn giữa cấu hình trình duyệt, đối tượng trang và kịch bản kiểm thử.
- **Bao phủ kịch bản đa dạng:** 13 Test Cases bao quát từ Bảo mật giao diện (UI Security), Kiểm tra ràng buộc (Validation), Chống tấn công dò mật khẩu (Anti-Brute Force với Captcha), Chuyển hướng SSO/OAuth, Phân tích giá trị biên (BVA) và Chịu tải buffer.
- **Phát hiện lỗi thực tế (Defect Detection):** Bắt được 01 lỗi thực tế của hệ thống (Lỗi không cắt bỏ khoảng trắng - WhiteSpace Trim Bug).
- **Báo cáo chuyên nghiệp:** Tích hợp báo cáo đồ họa **Allure Report** và xuất bảng báo cáo thực thi ra **Microsoft Excel** 2 sheet hoàn chỉnh.

---

## 🏗️ 2. Kiến trúc dự án (Page Object Model - POM)

```text
6451071041_VoThienLinh_KTPM_KT/
│
├── base/                              # TẦNG NỀN TẢNG (BASE LAYER)
│   ├── __init__.py
│   └── base_page.py                   # Wrapper class đóng gói WebDriver, WebDriverWait & tiện ích dùng chung
│
├── pages/                             # TẦNG ĐỐI TƯỢNG TRANG (PAGE OBJECT LAYER)
│   ├── __init__.py
│   └── login_page.py                  # Chứa toàn bộ Locators và Actions nghiệp vụ của trang Login UTC
│
├── tests/                             # TẦNG KỊCH BẢN KIỂM THỬ (TEST SCRIPT LAYER)
│   ├── __init__.py
│   ├── conftest.py                    # Quản lý fixture khởi tạo Chrome và hook chụp ảnh khi có lỗi
│   └── test_login_e2e.py              # Bộ 13 kịch bản kiểm thử E2E (TC01 -> TC13)
│
├── conftest.py                        # Fixture quản lý WebDriver ở root level
├── pytest.ini                         # File cấu hình Pytest (pythonpath & testpaths tự động)
├── requirements.txt                   # Danh sách thư viện phụ thuộc của dự án
├── export_to_excel.py                 # Script tự động xuất báo cáo kiểm thử ra Excel
├── BaoCao_Test_Login_UTC.xlsx         # Báo cáo thực thi kiểm thử 2 sheets (Dashboard + Chi tiết)
└── README.md                          # Tài liệu hướng dẫn dự án
```

---

## 🛠️ 3. Công nghệ và Thư viện sử dụng

| Công nghệ / Thư viện | Phiên bản | Mục đích sử dụng |
|---|---|---|
| **Python** | `3.13+` | Ngôn ngữ lập trình chính |
| **Selenium WebDriver** | `4.20+` | Tự động hóa thao tác trình duyệt Chrome |
| **PyTest** | `9.1+` | Framework quản lý và thực thi kiểm thử |
| **Webdriver Manager** | `4.0+` | Tự động tải ChromeDriver tương thích với trình duyệt |
| **Allure Framework** | `2.46+` | Tạo báo cáo kiểm thử trực quan với biểu đồ Dashboard |
| **OpenPyXL** | `3.1+` | Xây dựng và định dạng báo cáo kiểm thử ra file Excel |

---

## 📋 4. Danh sách 13 Kịch bản kiểm thử (Test Cases)

| Mã TC | Phân hệ / Loại kiểm thử | Tên kịch bản | Độ nghiêm trọng | Kết quả thực tế |
|---|---|---|---|---|
| **TC01** | UI / Security | Kiểm tra ô mật khẩu ẩn ký tự (`type='password'`) | Critical | **PASSED** |
| **TC02** | UI Interaction | Kiểm tra bật/tắt checkbox *'Giữ tôi luôn đăng nhập'* | Minor | **PASSED** |
| **TC03** | Form Validation | Bấm Đăng nhập khi để trống cả 2 ô | Normal | **PASSED** |
| **TC04** | Form Validation | Nhập Tên đăng nhập nhưng để trống Mật khẩu | Normal | **PASSED** |
| **TC05** | Form Validation | Để trống Tên đăng nhập nhưng có nhập Mật khẩu | Normal | **PASSED** |
| **TC06** | Authentication | Đăng nhập với tài khoản hoặc mật khẩu không chính xác | Critical | **PASSED** |
| **TC07** | Navigation | Kiểm tra điều hướng liên kết *'Bạn quên mật khẩu đăng nhập ?'* | Normal | **PASSED** |
| **TC08** | SSO / OAuth | Kiểm tra điều hướng nút *'Đăng nhập bằng e-mail UTC'* | Normal | **PASSED** |
| **TC09** | Happy Path | Đăng nhập thành công với tài khoản thật | Blocker | **SKIPPED** *(Chờ TK thật)* |
| **TC10** | Security / Rate Limit | Kích hoạt mã bảo mật (Captcha) sau 3 lần sai liên tiếp | Critical | **PASSED** |
| **TC11** | Input Validation | Nhập toàn ký tự khoảng trắng (Space) | Normal | **FAILED** *(Phát hiện Bug)* |
| **TC12** | Boundary (BVA) | Kiểm tra dữ liệu biên dưới độ dài tối thiểu (1 ký tự) | Minor | **PASSED** |
| **TC13** | Stress / Buffer | Kiểm tra độ bền hệ thống với chuỗi cực dài (500 ký tự) | Normal | **PASSED** |

### 🐞 Chi tiết Bug phát hiện được tại `TC11`:
* **Mô tả:** Hệ thống không tự động loại bỏ khoảng trắng (Trim) trước khi gửi form.
* **Kỳ vọng:** Khi người dùng nhập toàn dấu cách `"   "`, hệ thống phải cắt bỏ và báo lỗi: *"Bạn chưa nhập tên đăng nhập"*.
* **Thực tế:** Hệ thống xem khoảng trắng là dữ liệu hợp lệ và gửi request lên Server, trả về: *"Tài khoản hoặc mật khẩu không đúng."*.

---

## ⚡ 5. Hướng dẫn cài đặt và Chạy kiểm thử

### Bước 1: Clone dự án về máy
```bash
git clone https://github.com/Vo-Thien-Linh/VoThienLinh_6451071041_KTPM.git
cd VoThienLinh_6451071041_KTPM
```

### Bước 2: Cài đặt các thư viện cần thiết
```bash
pip install -r requirements.txt
```

### Bước 3: Chạy kiểm thử tự động
- **Chạy toàn bộ test cases và xem log chi tiết trên terminal:**
  ```bash
  pytest -v
  ```
- **Chạy riêng 1 test case cụ thể (ví dụ test Captcha):**
  ```bash
  pytest -k "test_tc10_captcha_on_multiple_failed_attempts" -v
  ```

---

## 📊 6. Tạo và Xem Báo cáo kiểm thử

### 1. Báo cáo trực quan với Allure Report
1. **Chạy test và ghi dữ liệu Allure:**
   ```bash
   pytest --alluredir=allure-results -v
   ```
2. **Khởi chạy máy chủ xem Allure Dashboard trên trình duyệt:**
   ```bash
   allure serve allure-results
   ```

### 2. Báo cáo Microsoft Excel
Chạy lệnh sau để cập nhật lại file báo cáo Excel:
```bash
python export_to_excel.py
```
File **`BaoCao_Test_Login_UTC.xlsx`** sẽ được tạo tại thư mục gốc với 2 Sheet:
- **Sheet 1 (Tổng Quan & Thống Kê):** Bảng Dashboard thống kê số lượng, tỷ lệ đạt/lỗi, biểu đồ và thông tin kiểm thử.
- **Sheet 2 (Chi Tiết Test Cases):** Bảng log ghi nhận chi tiết 11 cột chuẩn đặc tả kiểm thử thực tế.

---

## 📜 7. Quy chuẩn Commit (Conventional Commits)

Lịch sử Git của dự án được commit bài bản theo từng Test Case:
- `test(ui): [TC01] verify password field masks characters`
- `test(ui): [TC02] verify Keep Me Signed In checkbox toggle`
- `test(validation): [TC03] verify validation errors when both fields are empty`
- `...`
- `test(bug): [TC11] detect defect where system does not trim whitespace characters (Failed)`
- `test(bva): [TC12] verify lower boundary value with 1-character input`
- `test(stress): [TC13] verify system robustness with maximum-length 500-character input`
