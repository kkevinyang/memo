# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import youtube_dl


def get_video_source(video_url):
    """
    根据youtube播放页网址，获取视频源
    """
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
    with ydl:
        result = ydl.extract_info(video_url, download=False)

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries'][0]
    else:
        # Just a video
        video = result

    source_url = video['url']
    print 'source_url:', source_url
    return source_url

video_url = 'https://www.youtube.com/watch?v=AYFTDpXVlGs'
source_url = get_video_source(video_url)
