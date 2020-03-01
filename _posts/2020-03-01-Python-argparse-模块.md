---
layout: post
current: post
cover:  assets/images/python.png
navigation: True
title: Python argparse 模块使用记录
date: 2020-03-01 20:01:01
tags: [python]
class: post-template
subclass: 'post python'
author: dexfire
---

以下代码是一个 Python 程序，它获取一个整数列表并计算总和或者最大值：

```python
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
```

![测试](assets/images/QQ截图20200301111111.png)