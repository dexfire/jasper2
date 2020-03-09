---
layout: post
current: post
cover:  python.jpg
navigation: True
title: 【QQ空间爬虫】关于QQ空间g_tk的生成方法的python实现
date: 2020-03-10 01:00:00
tags: [python, spider,dev]
class: post-template
subclass: 'post python, dev'
author: dexfire
comment: True
---

# 【QQ空间爬虫】关于QQ空间g_tk的生成方法的python实现

QQ空间中的许多API都需要使用一个名叫 `g_tk` 的请求参数，而实验中证明，如果这个参数错误，会直接导致访问失败，而实际必须参数中也仅仅只有`g_tk`和`qzonetoken`两个参数是授权必须的（当然还要提供cookie啦）。

那么这个 `g_tk` 是怎样生成的呢？

我们首先打开QQ空间，发现QQ动态数据是动态加载的，那么一定涉及到了 XHR 请求，也就是在js代码中使用HTTP请求动态调用了数据，我们使用开发工具 Network 监视调用，发现向下刷新时，QQ空间网页请求了这样一个资源：

`https://user.qzone.qq.com/proxy/domain/ic2.qzone.qq.com/cgi-bin/feeds/feeds_html_act_all?uin=【你的QQ号】&hostuin=【当前访问用户的QQ号】&scope=7&filter=all&flag=1&refresh=0&firstGetGroup=0&mixnocache=0&scene=0&start=10&count=10&sidomain=qzonestyle.gtimg.cn&useutf8=1&outputhtmlfeed=1&refer=specialcare&r=0.7234408300556543&g_tk=70237777&qzonetoken=【QQ空间加密口令】&g_tk=70237777`

其中包含了`g_tk`字段，而这个参数并非Cookie的一部分，所以我们进一步尝试在 Source 中搜索这个关键字，发现并没有找到，那么可以推断，这个`g_tk`字段是在独立js文件中进行的调用。

![Network监控日志](/assets/images/QQ截图20200310011158.png)

在新Tab中打开是这样的，其中可以看到html格式的动态信息！

![QQ动态feeds](/assets/images/QQ截图20200310011349.png)

我们继续观察，发现其中加载了一个名叫 `qzfl_v8_[version].js` 的文件，在其中我们找到了我们关注的 `g_tk` 关键字！

![qzfl_v8.js](/assets/images/QQ截图20200310011608.png)

![g_tk 的线索](QQ截图20200310011836.png)

发现其调用了一行 `"g_tk=" + QZFL.pluginsDefine.getACSRFToken(t);` 显然，这正是我们关心的代码，跟踪其调用，发现这个关键函数的定义：
似乎已经发掘到矿山深处，开心！！(\*^▽^\*)
```js
QZFL.pluginsDefine.getACSRFToken = function(e) {
    e = QZFL.util.URI(e);
    var t;
    if (e) {
        if (e.host && e.host.indexOf("qzone.qq.com") > 0) {
            try {
                t = parent.QZFL.cookie.get("p_skey")
            } catch(e) {
                t = QZFL.cookie.get("p_skey")
            }
        } else if (e.host && e.host.indexOf("qq.com") > 0) {
            t = QZFL.cookie.get("skey")
        }
    }
    if (!t) {
        t = QZFL.cookie.get("p_skey") || QZFL.cookie.get("skey") || QZFL.cookie.get("rv2") || ""
    }
    return arguments.callee._DJB(t)
};
```

这里使用了一个 `arguments.callee` 引用，在 js 语法中，这个引用指向当前调用的函数体，也就是 `QZFL.pluginsDefine.getACSRFToken` 这个对象，但这个 `._DJB()` 又是个什么函数呢？我们继续挖掘！

结果就在这个函数体下方，我们看到这样一个函数定义：

```js
QZFL.pluginsDefine.getACSRFToken._DJB = function(e) {
    var t = 5381;
    for (var n = 0,
    r = e.length; n < r; ++n) {
        t += (t << 5) + e.charCodeAt(n)
    }
    return t & 2147483647
};
```

嘿嘿嘿，剩下的都是基本算法和基本函数，我们就可以用自己的代码来实现这个函数的移植版本啦！值得注意的是，这里第一个函数，使用了一个名为 `p_skey` 的cookie值，需要从浏览器中提取，提取方法是在QQ空间页面请求中 Network 中，查看html主页面的请求Cookie项，这里使用的是：
`pskey = 'Reo7rMXWccIn0wX4vy3PqkhcmGx93k6c7JTWjWfseVg_'`

我们在 Python IDLE 中进行试验：

```python
>>> def gen_gtk(p_skey):
    # function(e) {
    #     var t = 5381;
    #     for (var n=0,
    #          r=e.length; n < r; ++n) {
    #         t += (t << 5) + e.charCodeAt(n)
    #     }
    #     return t & 2147483647
    # };
    t = 5381
    for i in p_skey:
        t += (t) << 5 + ord(i)
    return t & 2147483647

>>> pskey = 'Reo7rMXWccIn0wX4vy3PqkhcmGx93k6c7JTWjWfseVg_'
>>> gen_gtk(pskey)
5381
>>>
```

结果呢，发现有什么不对劲，明明刚刚调用的 URL 中使用的是很长一串的才对？
`...300556543&g_tk=70237777&qzonetoken=...` 这个才是原版？

哪里的bug呢？捏死它丫的！

...
↑ 此处省略var个字...

结果还是基本功不扎实，这里的移位操作符优先级是低于加法的，所以要优先移位必须加括号，也就是如下版本：

```python
>>> def gen_gtk(p_skey):
    # function(e) {
    #     var t = 5381;
    #     for (var n=0,
    #          r=e.length; n < r; ++n) {
    #         t += (t << 5) + e.charCodeAt(n)
    #     }
    #     return t & 2147483647
    # };
    t = 5381
    for i in p_skey:
        t += (t << 5) + ord(i)
    return t & 2147483647

>>> gen_gtk(pskey)
635563388
>>>
```

这就对了噻！和我们源 URL 中的结果完全一致！！我滚去继续爬后续代码了...！

另：今晚 00:45 分有前后N年来难得一见的大月亮出现，纪念。