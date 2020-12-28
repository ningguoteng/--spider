# -*- coding:utf-8 -*-
import re

import requests
import jsonpath

def qushuiyin(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'
    }
    response = requests.get(url,headers=headers,allow_redirects=False)
    location_ = response.headers['Location']
    video_id = re.search(r'/video/(\d+)/', location_)
    items_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={video_id.group(1)}'

    response1 = requests.get(items_url, headers=headers, allow_redirects=False)
    response1_json = response1.json()


    video_url =jsonpath.jsonpath(response1_json,'$..play_addr.url_list')[0][0]
    video_url = video_url.replace('playwm','play')
    print(video_url)

    headers1 = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }

    response2 = requests.get(video_url, headers=headers1)
    with open('1.mp4','wb') as f:
        f.write(response2.content)



if __name__ == '__main__':
    url = 'https://v.douyin.com/JqJFYkY/'
    qushuiyin(url)



