---
layout: post
current: post
cover:  python.png
navigation: True
title: 【Python基础】日志处理之logging模块
date: 2020-03-17 23:10:00
tags: [python, dev]
class: post-template
subclass: 'post python, dev'
author: dexfire
comment: True
---

# 【Python基础】日志处理之logging模块

logging 是 Python 内建的实用日志输出模块，可以为应用与库定义了实现灵活的事件日志系统的函数与类.

使用标准库提提供的 logging API 最主要的好处是，所有的 Python 模块都可能参与日志输出，包括你的日志消息和第三方模块的日志消息。

这个模块提供许多强大而灵活的功能。如果你对 logging 不太熟悉的话， 掌握它最好的方式就是查看它对应的教程。

该模块定义的基础类和函数都列在下面。

- 记录器[`Logger`]暴露了应用程序代码直接使用的接口。
- 处理程序[`Handler`]将日志记录（由记录器创建）发送到适当的目标。
- 过滤器[`Filter`]提供了更精细的设施，用于确定要输出的日志记录。
- 格式化程序[`Formatter`]指定最终输出中日志记录的样式。

[Python 文档： logging --- Python 的日志记录工具](https://docs.python.org/zh-cn/3/library/logging.html?highlight=argparse#logging.Formatter)

## logging 测试代码

```python
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import logging
>>> r = logging.getLogger('log')
# 测试一下异常处理
>>> r.exception(None)
None
NoneType: None
>>> r.exception(BaseException('OK!'))
OK!
NoneType: None

>>> r.exception()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    r.exception()
TypeError: exception() missing 1 required positional argument: 'msg'

# 日志文件输出
>>> r.setLevel(logging.INFO)
>>> fmt = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
>>> fg = logging.FileHandler(".\\a.log",encoding='utf8')
>>> fg.setLevell(logging.DEBUG)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    fg.setLevell(logging.DEBUG)
AttributeError: 'FileHandler' object has no attribute 'setLevell'
>>> fg.setLevel(logging.DEBUG)
>>> fg.setFormatter(fmt)
>>> r.addHandler(fg)

# 设置以后，终端讲不再看到 日志输出
>>> r.info('Hello')
>>> r.setLevel(logging.INFO)
>>> r.info(hello)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    r.info(hello)
NameError: name 'hello' is not defined
>>> r.info("Hello, Foolish Logging.")
>>> 
```

## 输出结果

**输出：** a.log

```log
2020-03-17 23:06:46,292 <pyshell#12>[line:1] INFO Hello
2020-03-17 23:07:39,933 <pyshell#15>[line:1] INFO Hello, Foolish Logging.
```
