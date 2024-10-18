# secret_fileファイルは公開しない（gitignore）ファイルだから、ファイルがなくてロードされなければパスする
try:
    from .secret_file.py import API_KEY, CLIENT_ID, SPREADSHEET_ID
except ImportError:
    pass

import os

# DEBUG = Trueだとエラー内容が詳細に出てしまいトークン情報などが漏れる可能性があるため、Falseの場合のみ読み込む
# os.environを使えばこのプログラム上でのみ働く環境変数として設定できる（OSの環境には影響しない）
if not DEBUG:
    os.environ['API_KEY']        = API_KEY
    os.environ['CLIENT_ID']      = CLIENT_ID
    os.environ['SPREADSHEET_ID'] = SPREADSHEET_ID

require('dotenv').config();  // 環境変数の設定を読み込む
const fs = require('fs');
let config = {};

try {
  // local_secret_settingsファイルを読み込み、設定を反映
  const secretSettings = require('./secret_file');
  config = {
    API_KEY: secret_file.API_KEY,
    CLIENT_ID: secret_file.CLIENT_ID,
    SPREADSHEET_ID: secret_file.SPREADSHEET_ID
  };
} catch (error) {
  console.error("secret_fileファイルが見つかりませんでした。");
}

// DEBUGがFalseなら環境変数に設定する
const DEBUG = process.env.DEBUG === 'true';  // 環境変数DEBUGをチェック

if (!DEBUG) {
  process.env.API_KEY = config.API_KEY;
  process.env.CLIENT_ID = config.CLIENT_ID;
  process.env.SPREADSHEET_ID = config.SPREADSHEET_ID;
}
