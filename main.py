#!/usr/bin/python3

from __future__ import unicode_literals
import yt_dlp
import subprocess
import sys
import os
import yaml
import argparse

# コマンドライン引数解析
parser = argparse.ArgumentParser()

parser.add_argument("--CONFIG_PATH")
parser.add_argument("--CHANNEL_PATH")
args = parser.parse_args()

# 引数にファイルのPATH指定があればそれを使う、なければ実行ファイルと同じ階層に物を使う

if args.CONFIG_PATH is None:
    CONFIG_PATH = os.path.dirname(__file__)+"/yt-dlp_conf.yaml"
    with open(CONFIG_PATH,encoding="utf-8") as f:
        CONFIG_DICT = yaml.safe_load(f)
else:
    CONFIG_PATH = args.CONFIG_PATH

if args.CHANNEL_PATH is None:
    CHANNEL_PATH = os.path.dirname(__file__)+"/channels.yaml"
    with open(CHANNEL_PATH,encoding="utf-8") as f:
        CHANNEL_DICT = yaml.safe_load(f)
else:
    CHANNEL_PATH = args.CHANNEL_PATH

if "match_filter" in CONFIG_DICT:
    match_filter_text = CONFIG_DICT["match_filter"]
    CONFIG_DICT["match_filter"] =  yt_dlp.utils.match_filter_func(match_filter_text)

ydl_opts = CONFIG_DICT
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(CHANNEL_DICT)
    # ydl.download(['https://www.youtube.com/watch?v=Rk6rtktdDb4'])
    # ydl.download(['https://www.youtube.com/channel/UCM_I_CWRcp20EkrAKa7HUlA'])
