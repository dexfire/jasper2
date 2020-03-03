import argparse
import datetime

"""
用于产生一个新的 Post 文件，自动分类
"""

ap = argparse.ArgumentParser(
    "blog_new_post", epilog="a script to create new Jekyll Post.")
ap.add_argument("--title", "-t", dest="title", action="store", type=str)
ap.add_argument("--tags", dest="tags", nargs="*", action="store")

print(datetime.datetime())
