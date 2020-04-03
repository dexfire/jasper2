---
layout: post
current: post
cover:  python.png
navigation: True
title: 【Python】使用语句筛选和构建新的list, dict, set等集合
date: 2020-03-28 14:17:00
tags: [python, dev]
class: post-template
subclass: 'post python, dev'
author: dexfire
comment: True
---

# 【Python】使用语句筛选和构建新的list, dict, set等集合

List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

使用这种理解性语句，可以快速从已有的序列中构造新的序列，类似于lambda函数。


```python
>>> vec = [[0,1,3,345,4,5],[345,435,23,7],[34,45,66,4]]
>>> [n for elm in vec for n in elm]
[0, 1, 3, 345, 4, 5, 345, 435, 23, 7, 34, 45, 66, 4]
>>> [n for elm in vec if len(elm)>4 for n in elm]
[0, 1, 3, 345, 4, 5]
>>> [n for elm in vec if len(elm)>4 for n in elm if n>3]
[345, 4, 5]
>>> 
```

## 嵌套的理解性list构造

实现矩阵的转置。
```python
>>> matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        ]
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
>>> 
```

## 遍历器 `enmuerate() -> (idx, obj)`
```python
>>> for i,j in enumerate(range(5,10)):
	print(i,j)

0 5
1 6
2 7
3 8
4 9
```

## 其他类型的理解性语句

Sequence objects may be compared to other objects with the same sequence type. The comparison uses lexicographical ordering: first the first two items are compared, and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on, until either sequence is exhausted. If two items to be compared are themselves sequences of the same type, the lexicographical comparison is carried out recursively. If all items of two sequences compare equal, the sequences are considered equal. If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one. Lexicographical ordering for strings uses the Unicode code point number to order individual characters. Some examples of comparisons between sequences of the same type:
