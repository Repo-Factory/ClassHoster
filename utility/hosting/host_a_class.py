#!/usr/bin/env python3

from ROBOT_API import host_class
from multiprocessing import Process

def host_a_class(class_type):
    process = Process(target=host_class, args=[class_type])
    process.start()