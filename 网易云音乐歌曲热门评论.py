# coding: utf8
# @Author: 王均益
# @File: 网易云音乐歌曲热门评论.py
# @Time: 2017/4/30
# @Contact: 1223859299@qq.com
# @Description: 热门评论获取

import requests
import json

def getcomments(musicid):
    url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=5594eaee83614ea8ca9017d85cd9d1b3'.format(musicid)
    payload = {
        'params': '4hmFbT9ZucQPTM8ly/UA60NYH1tpyzhHOx04qzjEh3hU1597xh7pBOjRILfbjNZHqzzGby5ExblBpOdDLJxOAk4hBVy5/XNwobA+JTFPiumSmVYBRFpizkWHgCGO+OWiuaNPVlmr9m8UI7tJv0+NJoLUy0D6jd+DnIgcVJlIQDmkvfHbQr/i9Sy+SNSt6Ltq',
        'encSecKey': 'a2c2e57baee7ca16598c9d027494f40fbd228f0288d48b304feec0c52497511e191f42dfc3e9040b9bb40a9857fa3f963c6a410b8a2a24eea02e66f3133fcb8dbfcb1d9a5d7ff1680c310a32f05db83ec920e64692a7803b2b5d7f99b14abf33cfa7edc3e57b1379648d25b3e4a9cab62c1b3a68a4d015abedcd1bb7e868b676'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
        'Referer': 'http://music.163.com/song?id={}'.format(musicid),
        'Host': 'music.163.com',
        'Origin': 'http://music.163.com'
    }

    response = requests.post(url=url, headers=headers, data=payload)
    data = json.loads(response.text)
    hotcomments = []
    for hotcomment in data['hotComments']:
        item = {
            'nickname': hotcomment['user']['nickname'],
            'content': hotcomment['content']
        }
        hotcomments.append(item)



    # 返回热门评论
    return [content['content'] for content in hotcomments]

if __name__ == '__main__':
    hot = getcomments(439915614)
    print(hot)