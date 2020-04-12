import argparse
import re
import random
from datetime import datetime
import yaml
import os

"""
用于产生一个新的 Post 文件，自动分类
"""

sentences = ["From majestic mountains and valleys of en to crystal clear waters so blue, this wish is coming to you.",
             "越过青翠的峻岭和山谷，直到晶莹湛蓝的水边，飞来了我对你的祝愿。",
             "It's joy to know you, wishing the nicest things always for you, not only today, but all the year through ause you are really a joy to know.",
             "认识你是一种快慰，愿你永远拥有最美好的东西，不仅今天拥有，而且天天拥有，因为认识你真是一种慰藉。",
             "A friend is a loving companion at all times.",
             "朋友是永久的知心伴侣。",
             "When I think of you the miles between us disappear.",
             "当我想起你，相隔千里，如在咫尺。",
             "You're wonderful friend, and I treasure you more with every year.",
             "你是一位难得的挚友，我对你的珍重与岁俱增。",
             "Precious things are very few, That must be why there's just one for you.",
             "可贵的东西世间稀少，这正是为什么属于你的只有我一个。",
             "I love you more than I can say.",
             "我真不知该如何表达我对你的爱。",
             "Thinking of you still makes my heart beat fastest!",
             "想到你依然叫我心跳骤然加快 !",
             "You are in my thoughts every minute of the day, in my dream every hour of the night.",
             "白天，每分每秒我都在想念你，夜晚，每时每刻我都在梦见你。",
             "Think of me sometimes while Alps and ocean divide us, but they ever will, unless you wi** **. (Byron)",
             "长相思，天涯海角 ; 情不断，山水难隔。-- 拜伦",
             "You're everything to me.",
             "你是我的一切。",
             "With warmth and understanding at this time of sorrow and friendship that is yours for all the tomorrows.",
             "在这悲伤的时刻，请接受我的慰问和心意还有永远属于你的永恒的友谊。",
             "We would do anything to ease your sorrow if we only could.",
             "如果有可能，我们愿做任何事以稍释你的悲痛。",
             "I hope you can find a little comfort in the knowledge that your grief is shared by so many friends who are thinking of you.",
             "你知道吗 ?很多思念你的朋友在分担你的悲伤，希望你能感到安慰些。",
             "At this time of sorrow, deep sympathy goes to you and yours.",
             "在这悲戚的时刻，谨向你和你的亲人致以深切的慰问。",
             "Treasured memories live and grow more precious with time.",
             "May those beautiful yesterdays help to ease today's sorrow.珍爱的记忆与时光同在且日益珍贵，",
             "愿那些美好的昨天帮助你减轻今天的悲哀。",
             "May friends give you strength at this time of sorrow.",
             "May faith give you hope for every tomorrow.",
             "愿朋友们在你悲痛的时刻给你力量，",
             "愿信念给你的每一个明天带来希望。",
             "Though words cannot express the thoughts the heart would like to say, still may you know that others care and sympathize today.",
             "虽然言语不能表达内心欲诉的哀愁，",
             "仍愿你知道朋友们今天都为你分忧。",
             "Wishing you glad days filled with friendliness,",
             "Wishing you bright days filled with cheer,",
             "Wishing you warm days filled with happiness",
             "Wishing you to last throughout the year!",
             "Wishing you Have a wonderful brithday1",
             "愿你一年到头都有充满友谊的欢欣日子，",
             "愿你一年到头都有充满愉快的明朗日子，",
             "愿你一年到头都有充满幸福的温馨日子 !",
             "愿你一年到头都有祝你度过一个美妙的生日 !",
             "Roses, sweet and fragrant, sent to you to say, May each hour be a happy one on this special day.",
             "Have a happy birthday!",
             "送你一束甜蜜芬芳的玫瑰，她对你说，今天的喜庆分外美妙，每时每刻都同样幸福，令人陶醉。",
             "祝你生日快乐 !",
             "Every day is birthday time when thinking of you, and I shall keep one sublime hoping your many dreams come true.",
             "每当想到你我好似天天都在过生日，",
             "可我特别珍视其中的一天，",
             "祝愿你在这天美梦都能实现。",
             "The kindest friend there could ever be is the kind of friend you are to me.",
             "Happy Birthday!",
             "世上如有诤友，",
             "那就是像你对我那样关怀的朋友。",
             "祝你生日快乐 !",
             "Among the friends we make in life, there are only one or two who can be called a special friend and that's how I think of you.",
             "You show the warmth of your friendship in so many different ways, That's why I hope your birthday is the happiest of days.",
             "在我们结交的朋友中，",
             "只有一、二人堪称知已。我正是这样看你。",
             "你事无巨细都表现出温馨的友谊，",
             "为此我祝你生日幸福无比。",
             "Congratulations, Graduate, on all that you've accomplished",
             "Good luck in all that you'll achieve.",
             "祝贺你，毕业生，祝贺你取得的一切成绩.",
             "愿你日后一切顺利。",
             "Congratulations on your graduation!",
             "Wishing you a future filled with success and joy of seeing your dreams come true.",
             "It's such a pleasure to have a special reason to congratulate you.",
             "祝你学成毕业 !",
             "愿你前程似锦，事事如愿以偿。",
             "今日贺君有因，倍感欣慰欢畅 !",
             "Congratulations on your being graduated from high school.It's a wonderful feeling to have reached this milestone, and I envy you the opportunities that lie ahead.",
             "恭喜你毕业 ! 能达到这一段人生里程一定很兴奋吧，祝你前途无量 !",
             "Good luck, good health, hood cheer. I wish you a happy New Year.",
             "祝好运、健康、佳肴伴你度过一个快乐新年。",
             "With best wishes for a happy New Year!",
             "祝新年快乐，并致以良好的祝福。",
             "I hope you have a most happy and prosperous New Year.",
             "谨祝新年快乐幸福，大吉大利。",
             "With the compliments of the season.",
             "祝贺佳节。",
             "May the season's joy fill you all the year round.",
             "愿节日的愉快伴你一生。",
             "Season's GREetings and best wishes for the New Year.",
             "祝福您，新年快乐。",
             "Please accept my season's GREetings.",
             "请接受我节日的祝贺。",
             "To wish you joy at this holy season. Wishing every happiness will always be with you.",
             "恭祝新年吉祥，幸福和欢乐与你同在。",
             "Good health, good luck and much happiness throughout the year.恭祝健康、幸运，新年快乐。",
             "May the joy and happiness around you today and always.",
             "愿快乐幸福永伴你左右。",
             "Please accept my sincere wishes for the New Year. I hope you will continue to enjoy good health.",
             "请接受我诚挚的新年祝福，顺祝身体健康。",
             "Allow me to congratulate you on the arrival of the New Year and to extend to you all my best wishes for your perfect health and lasting prosperity.",
             "恭贺新禧，祝身体健康、事业发达。",
             "Best wishes for the holidays and happiness throughout the New Year.",
             "恭贺新禧，万事如意。",
             "With very best wishes for your happiness in the New Year.",
             "致以最良好的祝福，原你新年快乐幸福。",
             "Please accept our wishes for you and yours for a happy New Year.",
             "请接受我们对你及你全家的美好祝福，祝你们新年快乐。",
             "May the coming New Year bring you joy, love and peace.",
             "愿新年为你带来快乐，友爱和宁静。",
             "Wishing you happiness during the holidays and throughout the New Year.",
             "祝节日快乐，新年幸福。",
             "A happy New Year to you.",
             "恭贺新年。",
             "Season's GREetings and sincere wishes for a bright and happy New Year!献上节日的问候与祝福 , 愿你拥有一个充满生机和欢乐的新年。",
             "I give you endless brand-new good wishes. Please accept them as a new remembrance of our lasting friendship.",
             "给你我无尽的新的祝福，让它们成为我们永恒友谊的新的纪念。",
             "Good luck and GREat success in the coming New Year.",
             "祝来年好运，并取得更大的成就。",
             "On the occasion of the New Year, may my wife and I extend to you and yours our warmest GREetings, wishing you a happy New Year, your career greater success and your family happiness./zl",
             "在此新年之际，我同夫人向你及你的家人致以节日的问候，并祝你们新年快乐、事业有成、家庭幸福。", ]


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
    header.append(os.linesep)

    # ++++++++++++ 输出文件 ++++++++++++
    file_name = "_posts" + os.sep + dat + "-" + category_text + title + ".md"
    if os.path.exists(file_name):
        log_info("ERROR: file " + file_name + " is already exists!")
        exit(2)
    # log_info(file_name)
    with open(file_name, "a+", encoding=args.encoding, newline="") as fp:
        fp.write(os.linesep.join(header))
        fp.close()
        p = random.randint(0, len(sentences)-1)
        log_info("Successfully created post: " +
                 file_name + os.linesep + "::" + sentences[p])
