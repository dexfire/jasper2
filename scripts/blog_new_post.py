import argparse
import re
from datetime import datetime
import yaml
import os

"""
用于产生一个新的 Post 文件，自动分类
"""


def initArgParser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        "blog_new_post", epilog="Thanks for using. How about give me a Github Star at https://github.com/dexfire", description="a script to create new Jekyll Post. It will create a file named with date-[category][title or \"No.\"+number].md which contains a header of the filled columns infomation.", add_help=True)
    ap.add_argument("--title", "-t", dest="title",
                    action="store", type=str, help="The title of the post, optional.")
    ap.add_argument("--category", "-cg", dest="category", type=str,
                    required=False, default=None, help="The category name text. Default value is the first tag name.")
    ap.add_argument("--tags", "-tg", dest="tags", nargs="*", action="store", type=str,
                    help="The tag of the post, The first tag will use as the main category.")
    ap.add_argument("--datetime", "-dt", dest="datetime", type=str, default=None,
                    help="The post time, ISO format. format: 2020-05-20 00:00:00")
    ap.add_argument("--cover", "-c", dest="cover", type=str,
                    help="The post cover image, default to be the [first_tag_name].jpg.")
    ap.add_argument("--author", "-a", dest="author", type=str,
                    default="dexfire", required=False, help="The author of the post.")
    ap.add_argument("--nocomment", "-nc", dest="nocomment",
                    action="store_true", help="set if the post not allowed to comment.")
    ap.add_argument("--encoding", "-e", dest="encoding",
                    default="utf8", action="store", help="set the encoding of the file, default is utf8.")
    return ap


def log_info(msg):
    print("="*18 + " INFO " + "="*18 + os.linesep + msg+os.linesep + "="*42)


def getSequenceTitle() -> str:
    lists = os.listdir("_posts")
    pattern = r"\d{4}-\d{2}-\d{2}-(【.+?】){0,1}post_(\d{8}).md"
    ids = []
    for lis in lists:
        m = re.search(pattern=pattern, string=lis)
        if m is not None:
            # log_info(m.group(0))
            ids.append(int(m.group(2)))
    id_max = max(ids)
    return "post_{0:08}".format(id_max+1)


if __name__ == "__main__":
    # ++++++++++++ 初始化相关变量 ++++++++++++
    ap = initArgParser()
    args = ap.parse_args()
    # args = ap.parse_args(["-a", "dexfire", "-tg", "dev", "car"])
    authors = yaml.full_load(
        open(os.sep.join(['_data', 'authors.yml']), 'r', encoding='utf8'))
    config = yaml.full_load(open('_config.yml', 'r', encoding='utf8'))
    tags = yaml.full_load(
        open(os.sep.join(["_data", "tags.yml"]), encoding='utf8'))

    # ++++++++++++ 从参数中初始化变量 ++++++++++++

    # 作者
    author = args.author if args.author is not None else "dexfire"
    # 标题
    title = args.title if args.title is not None else getSequenceTitle()
    # log_info(title)
    # Tags
    if args.tags is not None:
        for tag in args.tags:
            err_list = []
            if tag not in tags:
                err_list.append(tag)
        if err_list > 0:
            log_info("ERROR tag: " + " ".join(err_list))
            print("Tags Available:\n\t", ' '.join(tags.keys()))
            exit(1)

    # 分类名
    category = args.category if (args.category is not None) else (
        tags[args.tags[0]]["name"] if (args.tags is not None
                                       and len(args.tags) > 0) else None)
    category_text = ("【" + category + "】") if (category is not None) else ""
    cover = tags[args.tags[0]
                 ]["cover"] if (args.tags is not None
                                and "cover" in tags[args.tags[0]]) else "False"
    # post时间
    dt_raw = datetime.fromisoformat(
        args.datetime) if args.datetime is not None else datetime.now()
    dat = dt_raw.strftime(r"%Y-%m-%d")
    dt = dt_raw.strftime(r"%Y-%m-%d %H:%M:%S")
    # ++++++++++++ 构建文本 ++++++++++++
    header = ["---"]
    header.append("layout: post")
    header.append("current: post")
    header.append("cover: " + cover)
    header.append("navigation: True")
    header.append("title: " + category_text + title)
    header.append("date: " + dt)
    header.append(
        "tags: " + "[" + (", ".join(args.tags) if args.tags is not None else "") + "]")
    header.append("class: post-template")
    header.append("subclass: '" + (" ".join(args.tags)
                                   if args.tags is not None else "") + "'")
    header.append("author: " + author)
    header.append("comment: True")
    header.append("")
    header.append("# " + category_text + title)
    header.append(os.sep)

    # ++++++++++++ 输出文件 ++++++++++++
    file_name = "_posts" + os.sep + dat + "-" + category_text + title + ".md"
    if os.path.exists(file_name):
        log_info("ERROR: file " + file_name + " is already exists!")
        exit(2)
    # log_info(file_name)
    with open(file_name, "a+", encoding=args.encoding) as fp:
        pass
