import requests
import re


# url = 'http://www.kuwo.cn/play_detail/325760'
url = "http://www.kuwo.cn/api/v1/www/music/playUrl?mid=325760"

response = requests.get(url)

print(response.text)
