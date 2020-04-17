import os
import filetype
import requests
import argparse

ap = argparse.ArgumentParser(
    "csdnimg", description="Upload an img to your CSDN account and print img foreign link.")
ap.add_argument(
    '-i', metavar='str', nargs='+', type=int,
    help='an integer to be summed')
