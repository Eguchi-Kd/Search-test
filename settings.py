# secret_fileファイルは公開しない（gitignore）ファイルだから、ファイルがなくてロードされなければパスする
try:
    from .secret_file.py import API_KEY, API_SECRET, ACCESS_KEY, ACCESS_SECRET
except ImportError:
    pass

import os

# DEBUG = Trueだとエラー内容が詳細に出てしまいトークン情報などが漏れる可能性があるため、Falseの場合のみ読み込む
# os.environを使えばこのプログラム上でのみ働く環境変数として設定できる（OSの環境には影響しない）
if not DEBUG:
    os.environ['API_KEY']       = API_KEY
    os.environ['API_SECRET']    = API_SECRET
    os.environ['ACCESS_KEY']    = ACCESS_KEY
    os.environ['ACCESS_SECRET'] = ACCESS_SECRET
