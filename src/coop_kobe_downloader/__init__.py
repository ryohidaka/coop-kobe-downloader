from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def main():
    downloader = CoopKobeDownloader()
    downloader.download()


class CoopKobeDownloader:
    def __init__(self):
        """
        CoopKobeDownloader クラスの初期化。
        """

        # ChromeDriverを取得
        try:
            self.driver = self._get_chrome_driver()
        except Exception as e:
            print(f"ChromeDriverの取得に失敗しました: {e}")
            self.driver = None

    def download(self):
        """
        ダウンロード処理
        """
        if self.driver is None:
            print("WebDriverが存在しないため、ダウンロード処理をスキップします。")

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
