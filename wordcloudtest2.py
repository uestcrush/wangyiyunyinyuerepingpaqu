# coding: utf8
# @Author: 王均益
# @File: 词云测试.py
# @Time: 2017/4/30
# @Contact: 1223859299@qq.com

# @Description: 词云测试
from wordcloud import WordCloud

import 网易云音乐热门评论 as hot
text = " ".join(hot.getcomments(132313))

wordcloud = WordCloud(random_state=1, font_path = r'C:/Users/Windows/fonts/simkai.ttf').generate(text)

import matplotlib.pyplot as plt
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()