#!/usr/bin/python3

from __future__ import unicode_literals
import yt_dlp

ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])