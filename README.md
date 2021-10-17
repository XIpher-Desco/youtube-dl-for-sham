# 何ができるか
チャンネルの動画を一括して保存する

# インストール手順
requirements.txt に記載されているパッケージをインストールします。
```
pip3 install -r requirements.txt
```

# 使い方
`yt-dlp_conf.yaml` と `channels.yaml` を sample から作る

デフォルト設定では、このディレクトリに ./youtube/channel/title.mp4 で保存される.  
保存先を変更するには、 yt-dlp_conf.yaml の path を変更する

## 実行
```
python3 ./main.py
```
