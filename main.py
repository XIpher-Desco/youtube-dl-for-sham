#!/usr/bin/python3

from __future__ import unicode_literals
import yt_dlp
import subprocess
import sys
import os
import yaml
import argparse

DEFAULT_CONFIG_PATH = os.path.dirname(__file__)+"/yt-dlp_conf.yaml"
DEFAULT_CHANNEL_PATH = os.path.dirname(__file__)+"/channels.yaml"

# コマンドライン引数解析
parser = argparse.ArgumentParser()

# 引数設定 CONFIG, CHANNEL PATH は指定があればそれを、無ければデフォルトを使う
parser.add_argument("--CONFIG_PATH", help="チャンネル一覧ファイルのフルパス,指定無ければ main.py と同じ階層の yt-dlp_conf.yaml を使用する" , nargs='?', const=DEFAULT_CONFIG_PATH, type=str, default=DEFAULT_CONFIG_PATH)
parser.add_argument("--CHANNEL_PATH", help="チャンネル一覧ファイルのフルパス,指定無ければ main.py と同じ階層の channels.yaml を使用する" , nargs='?', const=DEFAULT_CHANNEL_PATH, type=str, default=DEFAULT_CHANNEL_PATH)
args = parser.parse_args()

CONFIG_PATH = args.CONFIG_PATH
with open(CONFIG_PATH,encoding="utf-8") as f:
    CONFIG_DICT = yaml.safe_load(f)

CHANNEL_PATH = args.CHANNEL_PATH
with open(CHANNEL_PATH,encoding="utf-8") as f:
    CHANNEL_DICT = yaml.safe_load(f)

if "match_filter" in CONFIG_DICT:
    match_filter_text = CONFIG_DICT["match_filter"]
    CONFIG_DICT["match_filter"] =  yt_dlp.utils.match_filter_func(match_filter_text)

ydl_opts = CONFIG_DICT
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(CHANNEL_DICT)
    # ydl.download(['https://www.youtube.com/watch?v=Rk6rtktdDb4'])
    # ydl.download(['https://www.youtube.com/channel/UCM_I_CWRcp20EkrAKa7HUlA'])
