#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import threading
import Queue


q = Queue.Queue
def product(arg):
    while True:
        q.put(str(arg)+"包子")

def consumer(arg):
    while True:
        print (arg, q.put())
        time.sleep(2)
for i in range(3):
    t = threading.Thread(target = product, args = (i, ))
    t.start()

for j in range(20):
    t = threading.Thread(target = consumer, args = (j, ))
    t.start()