#!/usr/bin/python3

from __future__ import unicode_literals
import yt_dlp
import subprocess
import sys
import os
import yaml

CONFIG_PATH = os.path.dirname(__file__)+"/yt-dlp_conf.yaml"
with open(CONFIG_PATH,encoding="utf-8") as f:
    CONFIG_DICT = yaml.safe_load(f)

CHANNEL_PATH = os.path.dirname(__file__)+"/channels.yaml"
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
