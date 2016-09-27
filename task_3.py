#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_1():
    i=1
    while i!=0:
        if wall_is_on_the_right()==True:
            i=0
        else:
            move_right()
    pass


if __name__ == '__main__':
    run_tasks()
