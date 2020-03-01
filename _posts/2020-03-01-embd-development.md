---
layout: post
current: post
cover:  assets/images/东方水光月.jpg
navigation: True
title: 嵌入式开发概述
date: 2020-03-01 00:57:00
tags: [embed]
class: post-template
subclass: 'post embed'
author: dexfire
---

# 嵌入式开发概述
@[toc](目录)
## 嵌入式开发特点
![嵌入式系统特点](https://img-blog.csdnimg.cn/20200224081648925.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1FRMjc1MTc2NjI5,size_16,color_FFFFFF,t_70)
- 使用开发板开发，提供相关的底层工具
极少有直接拿一个ARM CPU来做开发，尽量让工程师的开发面向功能。
- 交叉式开发
PC端编译，嵌入式硬件式上运行，编译调试都要配置环境。
- 调试可能需要特定环境开发
比如温度测试功能，几千度的温度怎么仿真？
了解硬件
- 调试模式
一般使用仿真器进行开发， 需要硬件、调试器相互配合，不一定是通用的（JTAG是跨平台的）
![宿主机-目标机 调试模式](https://img-blog.csdnimg.cn/20200224081734724.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1FRMjc1MTc2NjI5,size_16,color_FFFFFF,t_70)
## 嵌入式系统开发流程
- 层级结构
	- 执行装置：被控对象（电机）
	- 功能层
		- 应用程序
	- 软件层
		- 文件系统
		- 图形用户接口
		- 任务管理
	- 实时操作系统（RTOS）
	- HAL、BSP 硬件抽象层
	排除许多硬件相关，多变的操作（地址、中断等）。方便跨平台。
	- 硬件层
		- MCU
		- 通用接口
		- 人机交互接口
		-
			-
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200224081938174.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1FRMjc1MTc2NjI5,size_16,color_FFFFFF,t_70)
- HAL、BSP 硬件抽象层

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200224082409391.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1FRMjc1MTc2NjI5,size_16,color_FFFFFF,t_70)
## UML 通用建模语言工具
UML是一个通用化的工具，可用于形成规范化的关系图谱，并形成相关的代码原型等。

### UML支持的图类别
- 用例图
- 类图
- 对象图
- 状态图
状态机，状态转移（有条件）
- 顺序图
- 协作图
- 活动图
- 组件图
- 部署图
![用例图](https://img-blog.csdnimg.cn/20200224084636578.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1FRMjc1MTc2NjI5,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200224084947391.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1FRMjc1MTc2NjI5,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020022408495783.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1FRMjc1MTc2NjI5,size_16,color_FFFFFF,t_70)