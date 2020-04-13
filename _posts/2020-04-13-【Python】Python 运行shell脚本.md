---
layout: post
current: post
cover: assets/images/Python.png
navigation: True
title: 【Python】Python 运行shell脚本
date: 2020-04-13 08:55:18
tags: [python, dev]
class: post-template
subclass: 'python dev'
author: dexfire
comment: True
---

# 【Python】Python 运行shell脚本
[15.1.5. Process Management - Python Docs](https://docs.python.org/2/library/os.html#process-management)

## 运行进程，替换当前进程
```python
os.execl(path, arg0, arg1, ...)
os.execle(path, arg0, arg1, ..., env)
os.execlp(file, arg0, arg1, ...)
os.execlpe(file, arg0, arg1, ..., env)
os.execv(path, args)
os.execve(path, args, env)
os.execvp(file, args)
os.execvpe(file, args, env)
```

These functions all execute a new program, replacing the current process; they do not return. On Unix, the new executable is loaded into the current process, and will have the same process id as the caller. Errors will be reported as OSError exceptions.

The current process is replaced immediately. Open file objects and descriptors are not flushed, so if there may be data buffered on these open files, you should flush them using sys.stdout.flush() or os.fsync() before calling an exec* function.

## 运行子进程
```python
os.spawnl(mode, path, ...)
os.spawnle(mode, path, ..., env)
os.spawnlp(mode, file, ...)
os.spawnlpe(mode, file, ..., env)
os.spawnv(mode, path, args)
os.spawnve(mode, path, args, env)
os.spawnvp(mode, file, args)
os.spawnvpe(mode, file, args, env)
```
Execute the program path in a new process.

(Note that the subprocess module provides more powerful facilities for spawning new processes and retrieving their results; using that module is preferable to using these functions. Check especially the Replacing Older Functions with the subprocess Module section.)

## 运行文件，并返回交互管道(pipeline)
```python
os.popen(...)
os.popen2(...)
os.popen3(...)
os.popen4(...)
```

Run child processes, returning opened pipes for communications. These functions are described in section File Object Creation.

如何在Python中启动后台进程？

我正在尝试将shell脚本移植到更具可读性的python版本。原始shell脚本启动几个进程(实用程序、监视器等)在“&”的背景中。如何在python中实现同样的效果？当python脚本完成时，我希望这些进程不要死。我确信这与守护进程的概念有某种关系，但我无法轻松找到如何做到这一点。
