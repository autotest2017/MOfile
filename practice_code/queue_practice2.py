#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import Queue

#LIFO即Last in First Out,后进先出
q = Queue.LifoQueue()

for i in range(5):
    q.put(i)

while not q.empty():
    print q.get()
