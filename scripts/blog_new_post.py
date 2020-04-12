import argparse
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
                    required=False, default=None, help="The category name. Default value is the first tag name.")
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
    print("="*18+" INFO "+"="*18 + os.linesep + "="*42)
    # print('='*40)
    # print(authors.keys(), config.keys(), tags.keys())


if __name__ == "__main__":
    ap = initArgParser()
    args = ap.parse_args(["-a", "dexfire", "-t",
                          "An awesome post title.", "-tg", "foo", "bar"])

    authors = yaml.full_load(
        open(os.sep.join(['_data', 'authors.yml']), 'r', encoding='utf8'))
    config = yaml.full_load(open('_config.yml', 'r', encoding='utf8'))
    tags = yaml.full_load(
        open(os.sep.join(["_data", "tags.yml"]), encoding='utf8'))

    for tag in args.tags:
        if tag not in tags:
            print("ERROR tag:", tag)
            print("Tags Available:\n\t", ' '.join(tags.keys()))
            exit(1)

    fn = datetime.fromisoformat(args.datetime)
    if args.title is None:
        title = ""
    else:
        title = args.title

    with open(os.sep.join(["_posts"])) as fp:
        pass
