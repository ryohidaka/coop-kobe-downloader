import os
from coop_kobe_downloader.driver_helper import DriverHelper
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    login_id = os.environ.get("LOGIN_ID")
    password = os.environ.get("PASSWORD")

    downloader = CoopKobeDownloader(login_id, password)
    downloader.download("2024062")


class CoopKobeDownloader:
    def __init__(self, login_id: str, password: str):
        """
        CoopKobeDownloader クラスの初期化。
        """
        # 認証情報を定義
        self.login_id = login_id
        self.password = password

        # ChromeDriverを取得
        try:
            self.driver = self._get_chrome_driver()
        except Exception as e:
            print(f"ChromeDriverの取得に失敗しました: {e}")
            self.driver = None

        # 宅配ページの共通URLを定義
        self.base_url = "https://wwwckapp.coop-kobe.net"

    def download(self, phase: str):
        """
        ダウンロード処理
        """
        if self.driver is None:
            print("WebDriverが存在しないため、ダウンロード処理をスキップします。")

        # 宅配ページにログインする
        self._login()

        # 注文書をダウンロードする
        self._download_csv(phase)

        # ChromeDriverを閉じる
        self.driver.quit()

    def _get_chrome_driver(self) -> webdriver.Chrome:
        """
        ChromeのWebDriverを取得
        WebDriverはChromeDriverManagerを通じてインストールされる。

        Returns:
            webdriver.Chrome: ChromeのWebDriverインスタンス
        """
        try:
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install())
            )
            return driver
        except Exception as e:
            print(f"WebDriverのインスタンス作成に失敗しました: {e}")
            return None

    def _login(self):
        """
        宅配ページにログインする
        """
        helper = DriverHelper(self.driver)

        # ログイン画面に遷移
        login_url = f"{self.base_url}/login.html"
        helper.navigate_to_url(login_url)

        # ログインIDを入力
        input_login_id = helper.find_element(By.NAME, "LOGIN_ID")
        helper.input_form(input_login_id, self.login_id)

        # パスワードを入力
        input_password = helper.find_element(By.NAME, "LOGIN_PASS")
        helper.input_form(input_password, self.password)

        # ログインボタンをクリック
        login_button = helper.find_element(By.CLASS_NAME, "p-mypage-part-btn--action")
        helper.click_button(login_button)

    def _download_csv(self, phase: str):
        """
        注文書のCSVファイルをダウンロードする
        """
        helper = DriverHelper(self.driver)

        # 注文履歴詳細画面に遷移
        history_detail_url = (
            f"{self.base_url}/order/member/historydetail.html?kikaku_ymkai={phase}"
        )
        helper.navigate_to_url(history_detail_url)

        # ダウンロードボタンをクリック
        download_button = helper.find_element(
            By.CLASS_NAME, "p-order-history-detail-control__dl-btn"
        )
        helper.click_button(download_button)
