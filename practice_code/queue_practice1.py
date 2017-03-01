#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import Queue

#FIFO即First in First Out,先进先出
q = Queue.Queue(maxsize=0)  #maxsize=0时可不用写
for i in range(6):
    q.put(i)

while not q.empty():
    print q.get()