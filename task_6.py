#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    n=1
    while n!=0:
        if wall_is_beneath()==False:
            move_right(1)
        else:
            n=0
    i=1
    while i!=0:
        if wall_is_beneath()==True:
            move_right(1)
        else:
            i=0
    pass


if __name__ == '__main__':
    run_tasks()
