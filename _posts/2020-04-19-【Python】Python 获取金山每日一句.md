---
layout: post
current: post
cover: assets/images/Python.png
navigation: True
title: 【Python】Python 获取金山每日一句
date: 2020-04-19 10:06:09
tags: [python]
class: post-template
subclass: 'python'
author: dexfire
comment: True
---

# 【Python】Python 获取金山每日一句

可以考虑，使用每日一句，作为当日博客的随机图片流和头部每日箴言？

## 新版接口
- API接口：`http://sentence.iciba.com/index.php?c=dailysentence&m=getdetail&title={date}&_={time}`  
- 接口可获取范围：2018-01-01 ~ 今天
- 超出此范围可考虑旧版。
- 前一个参数，格式严格要求，后一个参数，可以忽略
- 返回值效果：
```json
{
    "errno": 0,
    "errmsg": "success",
    "sid": 3737,
    "title": "2020-04-19",
    "content": "Everything in excess is opposed to nature.",
    "note": "在自然中，一切事物过犹不及。",
    "translation": "新版每日一句",
    "picture": "https://v-sq.ks3-cn-beijing.ksyun.com/image/e5a1769d8504b9b604be4009464dc5d6.jpg",
    "picture2": "https://v-sq.ks3-cn-beijing.ksyun.com/image/b002c55be7ecdf2e255c471e661d8855.jpg",
    "picture3": "https://v-sq.ks3-cn-beijing.ksyun.com/image/44dc3480b7c2b011c89d265730189c44.jpg",
    "caption": "词霸每日一句",
    "tts": "https://v-sq.ks3-cn-beijing.ksyun.com/audio/5891c02985f1c3f4ca5a93b144d92e51.mp3",
    "tts_size": "",
    "s_pv": 3051,
    "sp_pv": 0,
    "love": 8,
    "s_content": "",
    "s_link": "",
    "period": 0,
    "loveFlag": 0,
    "tags": "",
    "keep": 0,
    "comment_count": 336,
    "last_title": "2020-04-18",
    "next_title": 0,
    "week_info": [{
        "week": "Mon",
        "date": "2020-04-13",
        "flag": "show"
    },
    {
        "week": "Tue",
        "date": "2020-04-14",
        "flag": "show"
    },
    {
        "week": "Wen",
        "date": "2020-04-15",
        "flag": "show"
    },
    {
        "week": "Thu",
        "date": "2020-04-16",
        "flag": "show"
    },
    {
        "week": "Fri",
        "date": "2020-04-17",
        "flag": "show"
    },
    {
        "week": "Sat",
        "date": "2020-04-18",
        "flag": "show"
    },
    {
        "week": "Sun",
        "date": "2020-04-19",
        "flag": "cur"
    }]
}
```

## 旧版接口
- API_URL: `http://open.iciba.com/dsapi/?date=2020-04-18`
- 获取范围：2018-01-01 ~ 今天
- 返回效果

```json
{
    "sid": "2830", 
    "tts": "2018-01-01-day", 
    "content": "Nobody can go back and start a new beginning, but anyone can start now and make a new ending.", 
    "note": "没有人可以回到过去重新开始，但谁都可以从现在开始，书写一个全然不同的结局。", 
    "love": "10154", 
    "translation": "词霸小编：有一只牛站在海边，一只螃蟹看到了说：“牛耶！”这时候一个大浪拍在牛身上，螃蟹说：“海披牛耶！”Happy New Year! 新年快乐！", 
    "picture": "20180101.jpg", 
    "picture2": "big_20180101b.jpg", 
    "caption": "词霸每日一句", 
    "dateline": "2018-01-01", 
    "s_pv": "0", 
    "sp_pv": "0", 
    "fenxiang_img": "http://course-bj.ks3-cn-beijing.ksyun.com/image/old_sentence_bg.png", 
    "picture3": "xiaomi_20180101mi.jpg", 
    "picture4": "big_20170101pc.jpg", 
    "tags": [ ]
}
```

## 运行效果

`>>> get_daily()`  

> 在自然中，一切事物过犹不及。  
> Everything in excess is opposed to nature.

## 完整代码
```python
# coding=utf8
import requests
import time
import json


def get_daily():
    # api_url = "http://open.iciba.com/dsapi/"
    # eg. title=2020-04-19&_=1587261290
    api2_url = "http://sentence.iciba.com/index.php?c=dailysentence&m=getdetail&title={date}&_={time}"
    resp = requests.get(api2_url.format(date=time.strftime(
        "%Y-%m-%d"), time=str(int(time.time()))))
    if resp.ok:
        obj = json.loads(resp.text)
        print(obj["note"])
        print(obj["content"])
    else:
        print("获取失败！")


if __name__ == "__main__":
    get_daily()

```