#coding：utf-8
#@Author：王均益
#@File：网易云音乐热门评论
#Time：2017/4/30
#Description：热门评论获取
#爬取歌曲：李玉刚


import requests
import json

def getcomments(musicid):
    url="http://music.163.com/weapi/v1/resource/comments/R_SO_4_132313?csrf_token=b1662984e68d53baf60b5aa9889cca88".format(musicid)
    payload={
        'params':'KyIRa1vwcNczjLYTAC2U1dx3SctYjXkxRi6DfJ2gfU15jCiSWwkJzQr9QeIVEp7z48zUbfJ8yrxkjwDtl4Gfhqv8IVEYb5Q3+WajFnNAyumv5a3c6DOLu0y9gCAci3HYp2/C/dzIz0EMRyHrwP7KsYYIH+F8tvD+EZuBMmKb4uFwBAbqmxpCoivWpeWFx46rhEEUQoZw1jwbao8I2jKZZzFxiDYGq8zNJuYzGYdcmaA=',
        'encSecKey':'6586fe8a72a9deb442e4beeff088df42fe75071039a0117900c690373458da7bdbb9cd45d0a5b8ef3cd5b38c35c383cf9bc01f5fec29d8b5a9ce9d0bb9ce591cb1f8669f26ac732efa8f7de62669be3379f03daf4f07a386139936baafc7460eaa043e0901a280cdd7b92109143f205e6f4d2caaea90de3e605f092abba9534f'
    }
    headers={
      'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
      'Referer':'http://music.163.com/song?id={}'.format(musicid),
      'Host':'music.163.com',
      'Origin':'http://music.163.com'
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


    #返回热门评论
    return [content['content'] for content in hotcomments]


if __name__ == '__main__':
    hot = getcomments(132313)
    print(hot)

