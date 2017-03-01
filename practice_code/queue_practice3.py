#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import Queue
import threading


class work(object):
    def __init__(self, hello, world):
        self.hello = hello
        self.world = world
        print u"work:", world
        return
    def __cmp__(self, other):
        return cmp(self.hello, self.world)

q = Queue.PriorityQueue()  #属于一个优先级队列

q.put(work(3, "level 3 work"))
q.put(work(10, "level 10 work"))
q.put(work(1, "level 1 work"))

def process_work(q):
    while True:
        next_work = q.get()
        print "for:", next_work.world
        q.task_done()  #意味着之前入队的一个任务已经完成

workers = [threading.Thread(target = process_work, args = (q, )),
           threading.Thread(target = process_work, args = (q, ))
           ]
for i in workers:
    i.setDaemon(True)
    i.start()

q.join()

