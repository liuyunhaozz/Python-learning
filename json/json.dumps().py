# 爬取网页上 json 格式文件后重新缩进以便于阅读

import os
import time
import requests
from bs4 import BeautifulSoup
import re
import json


bvid = 'BV1aM4y1g7mj'
url='https://api.bilibili.com/x/web-interface/view?bvid='+bvid
data=requests.get(url).json()
print(json.dumps(data,indent=4))
