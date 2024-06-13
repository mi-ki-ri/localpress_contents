# LocalPress_Uploader

## 概要

ポストをアップロードするスクリプトです。

posts フォルダの中の markdown ファイルを読み込み、Strapi などの API にポストをアップロードします。

upload 先は `content` フィールドです。

## 使い方

- API_URL と API_KEY をそれぞれ export してください。
- requirements.txt を `pip install` してください。
- コマンドプロンプトで `. ./upload.sh` を実行してください。
