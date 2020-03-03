import argparse

ap = argparse.ArgumentParser(
    "blog_new_post", epilog="a script to create new Jekyll Post.")
ap.add_argument("--title", dest="title", action="")
