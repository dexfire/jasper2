import argparse
import datetime

"""
用于产生一个新的 Post 文件，自动分类
"""

ap = argparse.ArgumentParser(
    "blog_new_post", epilog="Thanks for using. Thinking about give me a Github Star?\nhttps://github.com/dexfire", description="a script to create new Jekyll Post.", add_help=True)
ap.add_argument("--title", "-t", dest="title",
                action="store", type=str, help="The title of the post, optional.")
ap.add_argument("--tags", "-tg", dest="tags", nargs="*", action="store",
                help="The tag of the post, The first tag will use as the main category.")
ap.add_argument("--datetime", "-dt", dest="date_time", type=datetime.datetime,
                help="The post time used to be.")
ap.print_help()

print(datetime.datetime.fromisoformat("2020-03-03 19:22:00"))
print(datetime.datetime.now())
