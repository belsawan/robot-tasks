#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_7():
    i=1
    while i!=0:
        if wall_is_above()==True:
            move_right(1)
        else:
            if wall_is_beneath()==True:
                move_right(1)
            else:
                i=0


    pass


if __name__ == '__main__':
    run_tasks()
