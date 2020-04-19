# coding=utf8
import requests
import time
import json


def get_daily():
    # api_url = "http://open.iciba.com/dsapi/"
    # eg. title=2020-04-19&_=1587261290
    api2_url = "http://sentence.iciba.com/index.php?c=dailysentence&m=getdetail&title={date}&_={time}"
    resp = requests.get(api2_url.format(date=time.strftime(
        "%Y-%m-%d"), time=str(int(time.time()))))
    if resp.ok:
        obj = json.loads(resp.text)
        print(obj["note"])
        print(obj["content"])
    else:
        print("获取失败！")


if __name__ == "__main__":
    get_daily()
