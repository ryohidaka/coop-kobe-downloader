# coop-kobe-downloader

[![PyPI version](https://badge.fury.io/py/coop-kobe-downloader.svg)](https://badge.fury.io/py/coop-kobe-downloader)
![build](https://github.com/ryohidaka/coop-kobe-downloader/workflows/Build/badge.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

コープこうべの宅配の注文書(CSV)をダウンロードする Python パッケージ

## Installation

You can install this library using PyPI:

```shell
pip install coop-kobe-downloader
```

## 使用方法

```py
from coop_kobe_downloader import CoopKobeDownloader

# ログインID
login_id = "hoge@example.com"

# パスワード
password = "hogehoge"

# CSV出力先のディレクトリ
download_dir = ".output"

# ダウンローダーのインスタンスを作成
downloader = CoopKobeDownloader(login_id, password, download_dir)

# ダウンロード処理　(例: 2024年6月2週)
downloader.download("2024062")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
