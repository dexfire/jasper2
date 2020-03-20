---
layout: post
current: post
cover:  redis.png
navigation: True
title: 【redis】一、Redis 数据库入门初体验
date: 2020-03-19 09:16:00
tags: [redis, cs, dev]
class: post-template
subclass: 'post redis cs dev'
author: dexfire
comment: True
---

# 【redis】一、Redis 数据库入门初体验

Redis 是一个开源（BSD许可）的，内存中的数据结构存储系统，它可以用作数据库、缓存和消息中间件。 它支持多种类型的数据结构，如 字符串（strings）， 散列（hashes）， 列表（lists）， 集合（sets）， 有序集合（sorted sets） 与范围查询， bitmaps， hyperloglogs 和 地理空间（geospatial） 索引半径查询。 Redis 内置了 复制（replication），LUA脚本（Lua scripting）， LRU驱动事件（LRU eviction），事务（transactions） 和不同级别的 磁盘持久化（persistence）， 并通过 Redis哨兵（Sentinel）和自动 分区（Cluster）提供高可用性（high availability）。

> Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes with radius queries and streams. Redis has built-in replication, Lua scripting, LRU eviction, transactions and different levels of on-disk persistence, and provides high availability via Redis Sentinel and automatic partitioning with Redis Cluster.

简介：
> Redis 是一个开源的，使用 ANSI C 语言编写的，可基于内存亦可持久化的日志型 Key-Value数据库，提供多种语言的 API。 从2010年3月15日起，Redis的开发工作由VMware主持。从2013年5月开始，Redis的开发由Pivotal赞助。

- **Redis 中文官方网站**：[http://www.redis.cn/](http://www.redis.cn/)  
- **Redis 官网**：[https://redis.io/](https://redis.io/)

## Redis 为什么这么受欢迎？ ———— Redis 八大特性
1. 速度快
Redis 使用 C 语言实现;  
Redis 所有的数据均存储于内存中。

2. 持久化
Redis所有数据存储在内存中，对数据的更新将异步地保存到磁盘内。

3. 支持多种数据结构

Redis 支持五种数据结构： String, List, Hash, Set, Zset

4. 支持多种编程语言

支持 Java，php，Python，Ruby，Lua，Node.js

5. 功能丰富

除了支持五种数据结构以外，还支持**事务、流水线、发布/订阅、消息队列**等功能。

6. 轻量级源码

约23000行C语言源代码，相比于mysql，MongoDB，Oracle等应用级数据库少太多。

7. 主从复制

主服务器执行添加、修改、删除，从服务器执行查询。主从可以自动进行数据同步。

8. 高可用及可分布式
   - Redis-Sentinel (v2.8) 支持高可用性 
   - Redis-Cluster (v3.0) 支持分布式

