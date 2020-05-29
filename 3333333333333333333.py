#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import urllib
import urllib.request
import time

import threading

import requests


def postFeedBack():
    url = "http://www.baidu.com"


    f = requests.post(url) # 发送post


    result = f.text
    print("shoudao")
    return (type(result))
    # print(result)


if __name__ == "__main__":
    import time
    start=time.time()
    i=0
    tasks_number=1
    while i < tasks_number:
        t = threading.Thread(target=postFeedBack)
        t.start()
        i+=1
        st = int(random.uniform(0, 1))
        # print("sleep:", st)
        time.sleep(st)
    end=time.time()
    print(end-start,"看看时间是不是并发")
    print("over?")
