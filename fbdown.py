from __future__ import unicode_literals
import youtube_dl
import json


with youtube_dl.YoutubeDL() as ydl:
   url= ydl.extract_info('https://www.facebook.com/PenMovies/videos/%E0%A4%B0%E0%A5%8B%E0%A4%A1-%E0%A4%AA%E0%A4%B0-%E0%A4%9A%E0%A4%B2-%E0%A4%B0%E0%A4%B9%E0%A5%87-%E0%A4%B2%E0%A5%8B%E0%A4%97%E0%A5%8B%E0%A4%82-%E0%A4%95%E0%A5%8B-%E0%A4%95%E0%A4%B2%E0%A5%87%E0%A4%95%E0%A5%8D%E0%A4%9F%E0%A4%B0-%E0%A4%B8%E0%A4%BE%E0%A4%B9%E0%A4%AC-%E0%A4%A8%E0%A5%87-%E0%A4%AC%E0%A5%81%E0%A4%B2%E0%A4%BE%E0%A4%AF%E0%A4%BE/434020308005968/?__cft__[0]=AZVQ-uYLd7gQtfzER6Q_o8Sm_1J1LW-FNR2EtYd8OYMFEQ7UzTH2E5SY01nRDk5mTSQrvdFUo4E8bdCJsV7jCsFDSkvgl8WeCo8GEx0RWG4PlDF4BoxeCoyumUSontCjclcEAFEhSOk7pcc6lk08yfYDnY1w0YitCvOkFQz4u-eVqw',download=False)
   print(url["formats"][-1]["url"])
