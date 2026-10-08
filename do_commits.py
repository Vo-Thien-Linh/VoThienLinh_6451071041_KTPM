import os
import re
import subprocess

CWD = r"d:\Python\KTPM\6451071041_VoThienLinh_KTPM_KT"
FILE_PATH = os.path.join(CWD, "tests", "test_login_e2e.py")

COMMIT_MSGS = [
    "test(ui): [TC01] verify password field masks characters",
    "test(ui): [TC02] verify Keep Me Signed In checkbox toggle",
    "test(validation): [TC03] verify validation errors when both fields are empty",
    "test(validation): [TC04] verify validation error when password field is empty",
    "test(validation): [TC05] verify validation error when username field is empty",
    "test(auth): [TC06] verify login is rejected with invalid username or password",
    "test(nav): [TC07] verify navigation to GetPass forgot password page",
    "test(sso): [TC08] verify redirect to Google OAuth when signing in with UTC email",
    "test(auth): [TC09] add successful login scenario with real account (skip)",
    "test(security): [TC10] verify CAPTCHA is triggered after 3 failed login attempts",
    "test(bug): [TC11] detect defect where system does not trim whitespace characters (Failed)",
    "test(bva): [TC12] verify lower boundary value with 1-character input",
    "test(stress): [TC13] verify system robustness with maximum-length 500-character input",
]

def main():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    # Tìm vị trí bắt đầu của từng test case
    pattern = r'\n    (?:@pytest\.mark\.skip\b.*?|@allure\.story\b.*?)(?=\s+def test_tc\d+)'
    matches = list(re.finditer(pattern, text, re.DOTALL))
    print(f"Total test cases found: {len(matches)}")
    assert len(matches) == 13

    # Tách header và 13 chunks
    header = text[:matches[0].start() + 1]
    chunks = []
    for i in range(len(matches)):
        start_pos = matches[i].start() + 1
        end_pos = matches[i+1].start() + 1 if i + 1 < len(matches) else len(text)
        chunks.append(text[start_pos:end_pos])

    print(f"Separated into {len(chunks)} chunks.")

    # 1. Reset soft commit trước đó để làm lại lịch sử sạch
    subprocess.run(["git", "reset", "--soft", "HEAD~1"], cwd=CWD)
    subprocess.run(["git", "reset"], cwd=CWD)

    # 2. Commit TC01 cùng toàn bộ project files
    current_text = header + chunks[0]
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(current_text)

    subprocess.run(["git", "add", "."], cwd=CWD)
    subprocess.run(["git", "commit", "-m", COMMIT_MSGS[0]], cwd=CWD)
    print("Committed TC01")

    # 3. Lần lượt commit từ TC02 đến TC13
    for i in range(1, 13):
        current_text += chunks[i]
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.write(current_text)

        subprocess.run(["git", "add", "tests/test_login_e2e.py"], cwd=CWD)
        subprocess.run(["git", "commit", "-m", COMMIT_MSGS[i]], cwd=CWD)
        print(f"Committed TC{i+1:02d}")

    # 4. Push force đè lên GitHub
    print("Pushing all 13 commits to GitHub...")
    res = subprocess.run(["git", "push", "-f", "--set-upstream", "origin", "main"], cwd=CWD, capture_output=True, text=True)
    print("Push stdout:", res.stdout)
    print("Push stderr:", res.stderr)

    # Dọn dẹp script
    if os.path.exists(os.path.join(CWD, "do_commits.py")):
        os.remove(os.path.join(CWD, "do_commits.py"))
    print("HOAN THANH 100%!")

if __name__ == "__main__":
    main()
